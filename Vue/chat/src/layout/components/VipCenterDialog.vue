<script setup lang='ts'>
import {NIcon, NModal, NCarousel, NCarouselItem, useDialog, useMessage, NCountdown, NSpace, NButton, NRadioGroup, NRadio, NSpin, NSkeleton, CountdownInst } from 'naive-ui'
import {computed, watch, ref} from 'vue'
import {useBasicLayout} from '@/hooks/useBasicLayout'
import {useAppCatStoreWithOut, useAppStore, useAuthStore, useGlobalStoreWithOut} from '@/store'
import {CloseOutline} from "@vicons/ionicons5";
import {useRouter} from "vue-router";
import {SvgIcon} from "@/components/common";
import Account from './vip/Account.vue'

interface Pkg {
  id: number
  name: string
  coverImg: string
  des: string
  days: number
  rechargeType: number
  model3Count: number
  model4Count: number
  drawMjCount: number
  expireDateCn: string
  createdAt: Date
  price: number
}

defineProps<Props>();

const useGlobalStore = useGlobalStoreWithOut();
const loading = ref(false);
const appStore = useAppStore();
const theme = computed(() => appStore.theme);
const message = useMessage();
const authStore = useAuthStore();

import memberDarkBg from "@/assets/svg/package-dark-bg.svg";
import memberLightBg from "@/assets/svg/package-light-bg.svg";
import {fetchGetPackageAPI, fetchGetPackageTypeAPI} from "@/api/crami";
import {ResData} from "@/api/types";
import {fetchOrderBuyAPI, fetchOrderQueryAPI} from "@/api/order";
import wxpay from "@/assets/wxpay.png";
import alipay from "@/assets/alipay.png";
import QRCode from "@/components/common/QRCode/index.vue";
import {fetchGetQrCode} from "@/api/global";


interface Props {
  visible: boolean,
}

const {isMobile} = useBasicLayout()
const ms = useMessage()

const carouselRef = ref()
const activeTab = ref(0);
const activePackage = ref(0);
const currentIndex = ref(0);
const orderInfo = computed(() => useGlobalStore.orderInfo)
const url_qrcode = ref('')
const qrCodeloading = ref(true)
const redirectloading = ref(true)
const redirectUrl = ref('')
const active = ref(true)
const payType = ref('wxpay')
const POLL_INTERVAL = 1000

const bg = computed(() => theme.value === 'dark' ? memberDarkBg : memberLightBg);

const isWxEnv = computed(() => {
  const ua = window.navigator.userAgent.toLowerCase()
  return ua.match(/MicroMessenger/i) && ua?.match(/MicroMessenger/i)?.[0] === 'micromessenger'
})

const typeList = ref<{ id: number, name: string, }[]>([])
const packageList = ref<{ typeId: number }[]>([])

const handleSelect = (type: number) => {
  activeTab.value = type;
  timer.value && clearInterval(timer.value)
  countdownRef.value?.reset()
}

const plat = computed(() => payType.value === 'wxpay' ? '微信' : '支付宝')
const countdownRef = ref<CountdownInst | null>()

const orderId = ref('')
const timer = ref()

const payTypes = computed(() => {
  return [
    {label: '微信支付', value: 'wxpay', icon: wxpay, payChannel: 'wxpay'},
    {label: '支付宝支付', value: 'alipay', icon: alipay, payChannel: 'alipay'},
  ].filter(item => payChannel.value.includes(item.payChannel))
})

const payPlatform = computed(() => {

  const {payHupiStatus, payEpayStatus, payMpayStatus, payWechatStatus} = authStore.globalConfig

  if (Number(payWechatStatus) === 1)
    return 'wechat'

  if (Number(payMpayStatus) === 1)
    return 'mpay'

  if (Number(payHupiStatus) === 1)
    return 'hupi'

  if (Number(payEpayStatus) === 1)
    return 'epay'
  return null
})

const payChannel = computed(() => {
  const {payEpayChannel, payMpayChannel} = authStore.globalConfig
  if (payPlatform.value === 'wechat')
    return ['wxpay']

  if (payPlatform.value === 'epay')
    return payEpayChannel ? JSON.parse(payEpayChannel) : []

  if (payPlatform.value === 'mpay')
    return payMpayChannel ? JSON.parse(payMpayChannel) : []

  if (payPlatform.value === 'hupi')
    return ['wxpay']

  return []
})

const activeTabData = computed(() => {
  const data = typeList.value.find(item => item.id === activeTab.value);
  const packager = packageList.value.filter(item => item.typeId === activeTab.value) || {};
  return {
    ...data,
    package: packager
  }
})

const isRedirectPay = computed(() => {
  const {payEpayApiPayUrl} = authStore.globalConfig
  return (payPlatform.value === 'epay' && payEpayApiPayUrl.includes('submit')) || payPlatform.value === 'mpay'
})


const handleClose = () => {
  useGlobalStore.updateVipDialog(false)
  loading.value = false;
  useGlobalStore.updateOrderInfo({})
  timer.value && clearInterval(timer.value)
  timer.value = null;
}


const queryQrCode = async () => {
  return await fetchGetQrCode({keys: ['chatOnline']}).then(res => res.data.chatOnline)
}

//  在线客服
const handleChatOnline = async () => {
  const qrCode = await queryQrCode();
  if (!qrCode) {
    ms.info("请先前往后台管理系统【关注我们】页面配置在线客服系统地址后再使用！")
    return
  }
  window.open(qrCode, "_blank");
}


// 选择套餐
const handleCheckPackage = (data: any) => {
  activePackage.value = data.id;
  handlePayPkg(data)
}

async function handlePayPkg(pkg: Pkg) {
  if (!payChannel.value.length)
    message.warning('管理员还未开启支付！')
  await handleBuyGoods(pkg)
}


// 购买商品
async function handleBuyGoods(pkg: Pkg) {

  // 如果是微信环境判断有没有开启微信支付,开启了则直接调用jsapi支付即可
  if (isWxEnv.value && payPlatform.value === 'wechat' && Number(authStore.globalConfig.payWechatStatus) === 1) {
    if (typeof WeixinJSBridge == 'undefined') {

      if (document.addEventListener) {
        document.addEventListener('WeixinJSBridgeReady', onBridgeReady, false)
      } else if (document.attachEvent) {
        document.attachEvent('WeixinJSBridgeReady', onBridgeReady)
        document.attachEvent('onWeixinJSBridgeReady', onBridgeReady)
      }

    } else {
      const res: ResData = await fetchOrderBuyAPI({goodsId: pkg.id, payType: 'jsapi'})
      const {success, data} = res;
      success && onBridgeReady(data)
    }
    return
  }

  /* 其他场景打开支付窗口 */
  useGlobalStore.updateOrderInfo({pkgInfo: pkg})
  // useGlobalStore.updateGoodsDialog(false)
  // useGlobalStore.updatePayDialog(true)
  handleOpenDialog();
}


/* 请求二维码 */
async function getQrCode() {
  !isRedirectPay.value && (qrCodeloading.value = true)
  isRedirectPay.value && (redirectloading.value = true)
  let qsPayType = null
  qsPayType = payType.value
  if (payPlatform.value === 'wechat')
    qsPayType = isWxEnv.value ? 'jsapi' : 'native'

  try {
    const res: ResData = await fetchOrderBuyAPI({goodsId: orderInfo.value.pkgInfo.id, payType: qsPayType})
    const {data, success, message} = res

    if (!success) {
      return ms.error(message)
    }

    const {url_qrcode: code, orderId: id, redirectUrl: url} = data

    redirectUrl.value = url
    orderId.value = id
    url_qrcode.value = code
    qrCodeloading.value = false
    redirectloading.value = false
  } catch (error) {
    // useGlobal.updatePayDialog(false)
    qrCodeloading.value = false
    redirectloading.value = false
  }
}

/* 跳转支付 */
function handleRedPay() {
  window.open(redirectUrl.value)
}

const queryOrderStatus = async () => {
  if (!orderId.value)
    return
  const result: ResData = await fetchOrderQueryAPI({orderId: orderId.value})
  const {success, data} = result
  if (success) {
    const {status} = data
    if (status === 1) {
      timer.value && clearInterval(timer.value)
      ms.success('恭喜你支付成功、祝您使用愉快！')
      active.value = false
      authStore.getUserInfo()
      // setTimeout(() => {
      //     useGlobal.updatePayDialog(false)
      // }, 2000)
    }
  }
}

async function handleOpenDialog() {
  await getQrCode()
  timer.value && clearInterval(timer.value)
  countdownRef.value?.reset()
  timer.value = setInterval(() => {
    queryOrderStatus()
  }, POLL_INTERVAL)
}

function handleFinish() {
  ms.error('支付超时，请重新下单!')
  timer.value && clearInterval(timer.value)
  // useGlobal.updatePayDialog(false)
  // useGlobal.updateGoodsDialog(true)
}

watch(payType, () => {
  getQrCode()
  countdownRef.value?.reset()
})


function onBridgeReady(data: {
  appId: string;
  timeStamp: string;
  nonceStr: string;
  package: string;
  signType: string;
  paySign: string
}) {

  const {appId, timeStamp, nonceStr, package: pkg, signType, paySign} = data

  if (!appId) {
    message.warning('appId不能为空')
    return
  }

  WeixinJSBridge.invoke('getBrandWCPayRequest', {
        appId, // 公众号ID，由商户传入
        timeStamp, // 时间戳，自1970年以来的秒数
        nonceStr, // 随机串
        package: pkg,
        signType, // 微信签名方式：
        paySign, // 微信签名
      },
      (res: any) => {

        if (res.err_msg === 'get_brand_wcpay_request:ok') {

          message.success('购买成功、祝您使用愉快!')

          setTimeout(() => {
          	authStore.getUserInfo()
          	useGlobalStore.updateVipDialog(false)
          }, 500);

        } else {
          message.warning('您还没有支付成功哟！')
        }
      })
}


const getPackageType = async () => {
  typeList.value = await fetchGetPackageTypeAPI().then(res => res.data.rows?.map(item => {

    return {
      ...item,
      desc: item.desc.split('\n')
    }
  }));
  activeTab.value = typeList.value[0]?.id;
}

const getAllPackage = async () => {
  packageList.value = await fetchGetPackageAPI({status: 1, size: 50}).then(res => res.data.rows.map(item => {
    return {
      ...item,
      des: item.des.split('\n')
    }
  }));
}


const handleEnter = () => {
  getPackageType();
  getAllPackage();
}


const next = () => {
  if (currentIndex.value === activeTabData.value?.package.length) {
    return;
  }

  const toIndex = currentIndex.value += 4

  carouselRef.value.to(toIndex)
}
const prev = () => {

  if (currentIndex.value === 0) return;
  const toIndex = currentIndex.value -= 4
  carouselRef.value.to(toIndex);
}

</script>

<template>

  <NModal :show="visible"
          style=" max-width: 1280px; height: 74vh; width: 1280px;"
          :mask-closable="false"
          :on-after-enter="handleEnter"
          :on-after-leave="handleClose">
    <div class="bg-white rounded-[30px] dark:bg-[#242432] bg-no-repeat bg-top bg-origin-border bg-contain"
         :style="{backgroundImage: 'url(' + bg + ')' }">

      <div class="absolute top-3 right-3 cursor-pointer z-30" @click="handleClose">
        <NIcon size="26" :color="theme === 'dark' ? '#fff' : '#333'">
          <CloseOutline/>
        </NIcon>
      </div>

      <div class="pt-5  mt-6 w-full h-auto">
        <div>

          <Account></Account>

          <!-- tab-->
          <div class="ml-10 dark:bg-[#2C2C42] bg-[#f7f9fa] rounded-full flex justify-around items-center px-2 py-2 w-[340px]">
            <template v-if="typeList.length">
              <div v-for="item in typeList" class="px-8 py-2 cursor-pointer duration-300 ease rounded-full"
                   @click="handleSelect(item.id)"
                   :class="[activeTab === item.id ? 'dark:bg-[#3D3D54] bg-[#519EF5] text-[#fff]  dark:text-[#486FF3]' : '']">
                <p class="select-none text-[16px]">{{ item.name }}</p>
              </div>
            </template>
            <template v-else>
              <div class="flex justify-start items-center">
                <n-skeleton height="20px" width="40%" class="mt-1 ml-4" :sharp="false"/>
              </div>
            </template>
          </div>


        </div>

        <!-- 套餐详细描述-->
        <div class="flex justify-between w-full">

          <div class="dark:bg-[#2B2B40] w-auto mt-6 px-8 py-12 bg-[#f7f9fa] rounded-br-3xl rounded-tr-3xl rounded-bl-3xl"
              v-if="activeTabData?.title && activeTabData?.desc.length">
            <h3 class="text-lg text-center mb-4">{{ activeTabData?.title }}</h3>
            <ul>
              <li v-for="item in activeTabData?.desc" class="leading-10 flex items-center border-b border-[#737380]">
                <SvgIcon class="text-lg leading-10 text-[#FF6B1B] mr-2" icon="mingcute:check-2-fill"></SvgIcon>
                <p>{{ item }}</p>
              </li>
            </ul>
          </div>

          <div v-else class="w-1/4  mt-6 px-8 py-12">
            <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-1 lg:grid-cols-1 xl:grid-cols-1 2xl:grid-cols-1 ">

              <n-space vertical class="border border-gray-200 dark:border-gray-600 rounded hover:bg-neutral-100
          							 dark:bg-[#2B2B40] dark:hover:bg-[#2B2B40] px-4 py-2  pb-4">
                <n-skeleton height="20px" width="80%" class="mt-1 ml-6" :sharp="false"/>
                <n-skeleton height="20px" width="100%" class="mt-1" :sharp="false"/>
                <n-skeleton height="20px" width="100%" class="mt-1" :sharp="false"/>
                <n-skeleton height="20px" width="100%" class="mt-1" :sharp="false"/>
                <n-skeleton height="20px" width="100%" class="mt-1" :sharp="false"/>
                <n-skeleton height="20px" width="100%" class="mt-1" :sharp="false"/>
                <n-skeleton height="20px" width="100%" class="mt-1" :sharp="false"/>
                <n-skeleton height="20px" width="100%" class="mt-1" :sharp="false"/>
                <n-skeleton height="20px" width="100%" class="mt-1" :sharp="false"/>
                <n-skeleton height="20px" width="100%" class="mt-1" :sharp="false"/>
                <n-skeleton height="20px" width="100%" class="mt-1" :sharp="false"/>
              </n-space>
            </div>
          </div>

          <!--选择套餐-->
          <div class="flex flex-col w-3/4 mt-4 pr-8">
            <div class="w-full">

              <div class="flex justify-between items-center w-full mb-2">
                <h5 class="text-lg ml-4">选择会员套餐</h5>
                <p>充值即时到账，有任何疑问，可<span class="cursor-pointer text-[#FF6B1B]"
                                                   @click="handleChatOnline">联系客服</span></p>
              </div>

              <ul class="flex flex-row justify-around px-10 relative" v-if="activeTabData?.package.length">
                <!--                左侧侧切换按钮-->
                <button type="button" :disabled="currentIndex === 0"
                        class="absolute rounded-full hover:dark:bg-[#2C2C42] hover:bg-[#ccc] left-[-10px] top-1/2  "
                        @click="prev">
                  <SvgIcon icon="mingcute:left-line" class="text-[36px] text-[#888]"></SvgIcon>
                </button>

                <!-- 轮播套餐 -->
                <n-carousel
                    ref="carouselRef"
                    :loop="false"
                    :default-index="0"
                    :show-dots="false"
                    :show-arrow="false"
                    :space-between="10"
                    :slides-per-view="4"
                    draggable
                >

                  <n-carousel-item v-for="item in activeTabData?.package">

                    <li @click="handleCheckPackage(item)"
                        :class="[theme === 'light' ? 'light-active' : 'dark-active', item.id === activePackage ?
												'border-[#519EF5] bg-gradient-to-t from-[#519EF5] to-[#3278ED] text-white' : 'dark:border-[#39394B] bg-[#fff]  border-[#E5E5E5] dark:bg-[#27273B]']"
                        class="cursor-pointer select-none hover:border-[#519EF5] hover:bg-gradient-to-t from-[#519EF5] to-[#3278ED] hover:text-white relative  pb-[60px] w-full rounded-2xl border-2  flex flex-col px-2 py-4 ">

                      <h2 class="text-[14px] text-center mb-2">{{ item?.name }}</h2>
                      <h3 class="text-[14px] text-center mb-2 text-[#FF6B1B] flex justify-center items-center">
                        <SvgIcon icon="streamline:yuan-solid"></SvgIcon>
                        <span class="text-lg">  {{ item?.price }}</span>
                      </h3>
                      <div class="line-clamp-4 min-h-[80px]">
                        <p v-for="subItem in item?.des"
                           class="leading-0 dark:text-[#DFDFDF] flex flex-start items-center">
                          <SvgIcon class="text-lg leading-10 text-[#FF6B1B] mr-2"
                                   icon="mingcute:check-2-fill"></SvgIcon>
                          <span class="text-[12px]">{{ subItem }}</span>
                        </p>
                      </div>

                      <div
                          :class="[item.id === activePackage ? 'active-price-down text-white' : '']"
                          class="price-down w-full absolute bottom-0 py-2 left-0 rounded-br-xl rounded-bl-xl">
                        <p class="text-center">{{ item.name }}</p>
                      </div>
                    </li>
                  </n-carousel-item>
                </n-carousel>

<!--                右侧切换按钮-->
                <button type="button" :disabled="currentIndex === activeTabData?.package.length"
                        class="absolute rounded-full hover:dark:bg-[#2C2C42] hover:bg-[#ccc] right-0 top-1/2 text-white "
                        @click="next">
                  <SvgIcon icon="mingcute:right-line" class="text-[36px] text-[#888]"></SvgIcon>
                </button>

              </ul>

              <div v-else class="w-full">
                <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-1 lg:grid-cols-1 xl:grid-cols-4 2xl:grid-cols-4 gap-5">

                  <n-space vertical v-for="item in 4" class="border   rounded-2xl border-gray-200 dark:border-gray-600   hover:bg-neutral-100 dark:bg-[#2B2B40] dark:hover:bg-[#24272e] px-4 py-2  pb-4">
                    <n-skeleton height="20px" width="60%" class="mt-1 ml-9" :sharp="false"/>
                    <n-skeleton height="20px" width="40%" class="mt-1  ml-14" :sharp="false"/>
                    <n-skeleton height="20px" width="100%" class="mt-1" :sharp="false"/>
                    <n-skeleton height="20px" width="100%" class="mt-1" :sharp="false"/>
                    <n-skeleton height="20px" width="100%" class="mt-1" :sharp="false"/>
                    <n-skeleton height="20px" width="100%" class="mt-1" :sharp="false"/>
                  </n-space>

                </div>
              </div>

              <div class="mt-4 ml-4">
                <p>套餐说明:购买会员套餐获得对应有效期，套餐积分仅当月有效，跨月不叠加，请在有效期内及时使用</p>
              </div>
            </div>

            <div class="dark:bg-[#2B2B40] rounded-2xl  " v-if="orderInfo.pkgInfo?.price">

              <div class="p-4 ">

                <div class="flex flex-start"
                     :class="[isMobile ? 'flex-col' : 'flex-row', isRedirectPay ? 'flex-row-reverse' : '']">
                  <div>

                    <div class="flex items-center justify-center relative ">

                      <!-- qrCodeloading -->
                      <NSpin v-if="qrCodeloading && !isRedirectPay" size="large"
                             class="absolute left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2"/>

                      <NSkeleton v-if="qrCodeloading" :width="120" :height="120" :sharp="false" size="medium"/>

                      <!-- epay -->
                      <QRCode v-if="payPlatform === 'epay' && !qrCodeloading && !redirectloading && !isRedirectPay"
                              :value="url_qrcode" :size="120"/>
                      <img v-if="payType === 'wxpay' && !qrCodeloading && !isRedirectPay" :src="wxpay"
                           class="absolute left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2 w-10 bg-[#fff]">
                      <img v-if="payType === 'alipay' && !qrCodeloading && !isRedirectPay" :src="alipay"
                           class="absolute left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2 w-10 bg-[#fff]">

                      <!-- wechat -->
                      <QRCode v-if="payPlatform === 'wechat' && !qrCodeloading" :value="url_qrcode" :size="120"/>

                      <div v-if="isRedirectPay" class="flex flex-col"
                           :class="[isRedirectPay && isMobile ? 'ml-0' : 'ml-20']">
                        <span class="mb-10 mt-5 text-base">当前站长开通了跳转支付</span>

                        <!-- mapy 跳转支付 -->
                        <NButton v-if="isRedirectPay" type="primary" ghost :disabled="redirectloading"
                                 :loading="redirectloading" @click="handleRedPay">
                          点击前往支付
                        </NButton>
                      </div>

                      <!-- hupi -->
                      <iframe v-if="payPlatform === 'hupi' && !redirectloading" class="w-[120px] h-[120px] scale-90"
                              :src="url_qrcode" frameborder="0"/>
                    </div>

                  </div>
                  <div class=" flex flex-col " :class="[isMobile ? 'w-full ' : ' ml-10 w-[200] ']">

                    <div><span class="whitespace-nowrap font-bold">应付金额：</span> <i
                        class="text-xl text-[red] font-bold">{{ `￥${orderInfo.pkgInfo?.price}` }}</i></div>

                    <div style="white-space: nowrap" class="mt-4 w-full text-center font-bold text-sm"
                         :class="[isMobile ? 'mb-2' : 'mb-4']">
                      请在 <span class="w-[60px] inline-block text-[red] text-left"><NCountdown ref="countdownRef"
                                                                                                :active="active"
                                                                                                :duration="300 * 1000"
                                                                                                :on-finish="handleFinish"/></span>
                      时间内完成支付！
                    </div>

                    <NRadioGroup v-model:value="payType" name="radiogroup" class="flex">
                      <NSpace :vertical="!isMobile" justify="center" :size="isMobile ? 10 : 35" class="w-full">
                        <NRadio v-for="pay in payTypes" :key="pay.value" :value="pay.value">
                          <div class="flex items-center">
                            <img class="h-4 object-contain mr-2" :src="pay.icon" alt=""> {{ pay.label }}
                          </div>
                        </NRadio>
                      </NSpace>
                    </NRadioGroup>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </NModal>
</template>


<style lang="less" scoped>

.light-active {
  &:hover {
    .price-down {
      background: #3177ED;
    }
  }

  .price-down {
    background: #f7f7f7;
  }
}

.active-price-down {
  background: #3177ED !important;
}

.dark-active {
  &:hover {
    .price-down {
      background: #3177ED;
    }
  }

  .price-down {
    background: #39394B;
  }
}

</style>
