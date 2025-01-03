<script setup lang='ts'>
import type { CSSProperties } from 'vue'
import { computed, ref, watch,} from 'vue'
import type { NumberAnimationInst } from 'naive-ui'
import { NButton, NInput, NLayoutSider, NTabs, NTabPane, useDialog, useMessage } from 'naive-ui'
// import { useRouter } from 'vue-router'
import List from './List.vue'
import { SvgIcon } from '@/components/common'

import {useAppCatStoreWithOut, useAppStore, useAuthStore, useChatStore,  } from '@/store'
import { useBasicLayout } from '@/hooks/useBasicLayout'
// const useGlobalStore = useGlobalStoreWithOut()
const appCenterStore = useAppCatStoreWithOut()

// const router = useRouter()
const appStore = useAppStore()
const chatStore = useChatStore()
const authStore = useAuthStore()
const ms = useMessage()
const model3AnimationInstRef = ref<NumberAnimationInst | null>(null)
const model4AnimationInstRef = ref<NumberAnimationInst | null>(null)
// const userBalance = computed(() => authStore.userBalance)
const dialog = useDialog()

/* 当前选用的模型的扣费类型 1: 普通 2： 高级  */
// const activeModelKeyDeductType = computed(() => chatStore?.activeModelKeyDeductType)
// const activeModelKeyPrice = computed(() => chatStore?.activeModelKeyPrice)
const activeChatTab = computed(() => chatStore.activeChatTab)

const oldUse3Token = ref(0)
const newUse3Token = ref(0)
const oldUse4Token = ref(0)
const newUse4Token = ref(0)

const isSearch = ref(false)
const searchRef = ref(null)

watch(() => authStore.userBalance.useModel3Token, (newVal, oldVal) => {
  oldUse3Token.value = oldVal || 0
  newUse3Token.value = newVal || 0
  model3AnimationInstRef.value?.play()
}, {
  immediate: true,
  flush: 'post',
})

watch(() => authStore.userBalance.useModel4Token, (newVal, oldVal) => {
  oldUse4Token.value = oldVal || 0
  newUse4Token.value = newVal || 0
  model4AnimationInstRef.value?.play()
}, {
  immediate: true,
  flush: 'post',
})

const { isMobile } = useBasicLayout()
const addLoading = ref(false)

const collapsed = computed(() => appStore.siderCollapsed)
const groupKeyWord = ref('')

function handleInputGroupSearch(val: string) {
  groupKeyWord.value = val
  chatStore.setGroupKeyWord(val)
}

function handleBlurInput(){
	isSearch.value = false
}

// 提取公共的功能
function checkAuth(){
	if(!authStore.isLogin) {
		ms.info("请先登录")
		addLoading.value = false
		authStore.setLoginDialog(true);
		return false
	}
	 return true
}

/* 新增一个对话 */
async function handleAdd() {
  try {

    if(!checkAuth()) {
      return;
    }

    addLoading.value = true
    await chatStore.updateChatTab('history');
    await chatStore.addNewChatGroup()
    await chatStore.queryMyGroup()
    addLoading.value = false

    if (isMobile.value)
      appStore.setSiderCollapsed(true)
  }
  catch (error) {
    addLoading.value = false
  }
}

/* 删除全部非置顶聊天 */
async function handleDelGroup() {
	if(!checkAuth()) {
		return;
	}

  dialog.create({
    title: '清空分组',
    content: '是否删除所有非置顶的对话组？',
    positiveText: '确认删除',
    negativeText: '再想想',
    onPositiveClick: async () => {
      await chatStore.delAllGroup()
    },
  })
}

function handleUpdateCollapsed() {
  appStore.setSiderCollapsed(!collapsed.value)
}

const theme = computed(() => appStore.theme)


const getMobileClass = computed<CSSProperties>(() => {
  if (isMobile.value) {
    return {
      position: 'fixed',
      zIndex: 50,
			// left: 0,
			top: '56px',
			height: 'calc(100% - 56px)'
    }
  }

  return {
		background: theme.value ==='dark' ?  '#131323': '',
		height: 'calc(100% - 60px)'
	}
})

const mobileSafeArea = computed(() => {
  if (isMobile.value) {
    return {
      paddingBottom: 'env(safe-area-inset-bottom)',
    }
  }
  return {}
})

watch(() => isMobile.value, (val) => {
		appStore.setSiderCollapsed(val)},
  {
    immediate: true,
    flush: 'post',
  },
)
</script>

<template>
  <div>
    <NLayoutSider
      :collapsed="collapsed"
      :collapsed-width="0"
      :width="260"
      :show-trigger="false"
      collapse-mode="transform"
      :bordered="false"
      :style="getMobileClass"
      @update-collapsed="handleUpdateCollapsed"
    >
      <div class="flex flex-col h-full" :style="mobileSafeArea">
        <main class="flex flex-col h-full flex-1 min-h-0 dark:bg-[#131323] bg-[#FBFBFB]">

          <div class="flex h-14 items-center space-x-4 justify-between px-4 dark:bg-[#131323] bg-[#fafafa]" >

            <div class="flex-1">
              <button  class="rounded w-full px-2.5 py-1.5  flex justify-center items-center  bg-gradient-to-r  from-[#3076ED]
               to-[#54A2F5] hover:bg-gradient-to-r text-white" :loading="addLoading" @click="handleAdd">
                <SvgIcon icon="simple-line-icons:plus" class="text-sm mr-0.5" />
                <span class="mr-0">新建对话</span>
              </button>
            </div>

            <div class="flex-1">
              <button class="rounded w-full px-2.5 py-1.5 flex justify-center items-center bg-gradient-to-r from-[#3076ED] to-[#54A2F5] hover:bg-gradient-to-r text-white"
											@click="appCenterStore.updateAppCenterDialog(true)">
                <SvgIcon icon="iconoir:app-store" class="text-sm mr-0.5" />
                <span class="mr-0">应用中心</span>
              </button>
            </div>

          </div>

          <div class="my-2 mx-4">
            <NInput v-model="groupKeyWord" ref="searchRef" type="text" placeholder="对话历史查找" @blur="handleBlurInput"
                    clearable @input="handleInputGroupSearch"  >
              <template #prefix>
                 <SvgIcon icon="ion:search" class="text-xl" />
              </template>
            </NInput>
          </div>

          <div class="border-b border-gray-200 dark:border-gray-700">
            <n-tabs
                v-model:value="activeChatTab"
                class="card-tabs flex justify-center items-center"
                default-value="signin"
                size="medium"
                animated
                @update-value="chatStore.updateChatTab"
                pane-wrapper-style="margin: 0 -4px"
                pane-style="padding: 0 4px 0 4px; box-sizing: border-box;"
            >
              <n-tab-pane name="history"  tab="历史对话"></n-tab-pane>
              <n-tab-pane name="app"   tab="助手列表"></n-tab-pane>
            </n-tabs>
          </div>

					<!-- 对话分组 显示-->
          <div class="flex-1 mt-2 min-h-0 pb-4 overflow-hidden">
            <List />
          </div>

            <div class="flex justify-between border-t dark:border-gray-700 py-2">
              <NButton  :bordered="false" size="small" style="width: 100%" @click="handleDelGroup">
                <SvgIcon icon="ant-design:delete-outlined" class="ml-2 mr-2 text-sm" />
                <span class="mr-3">清空全部非置顶会话</span>
              </NButton>

          </div>
        </main>

      </div>
    </NLayoutSider>

    <template v-if="isMobile">
      <div v-show="!collapsed" class="fixed inset-0 z-40 bg-black/40 " @click="handleUpdateCollapsed" />
    </template>

  </div>
</template>
