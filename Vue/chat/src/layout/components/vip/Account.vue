<script setup lang="ts">
import {	NAvatar, } from 'naive-ui'
import defaultAvatar from "@/assets/avatar.png";
import {computed} from "vue";
import {useAuthStore} from "@/store";
import {SvgIcon} from "@/components/common";
const authStore = useAuthStore();

const isLogin = computed(() => authStore.isLogin);
const avatar = computed(() => authStore.userInfo.avatar);
const username = computed(() => authStore.userInfo.username);
const userBalance = computed(() => authStore.userBalance)
</script>

<template>
  <div class="flex flex-start items-center ml-8 mb-8 text-white">
    <NAvatar :size="60"
             :src="avatar"
             round
             bordered
             :fallback-src="defaultAvatar"
             class="cursor-pointer"
    />

    <div class="flex flex-col text-gray-500 dark:text-gray-300 ml-4">
      <div class="flex flex-start">
        <p class="select-none text-left text-md mb-1 text-[#fafafa]">当前用户：{{ username }}</p>
      </div>
      <div class="flex-row flex ">
        <div
            class="bg-gradient-to-r from-[#59A7F7] to-[#3075ED] rounded-tr-xl rounded-bl-xl px-3 py-1 w-max-18 mr-2">
          <p class="text-white text-center">{{ userBalance.expirationTime ? '已开通' : '未开通' }}</p>
        </div>
        <div class="flex justify-start items-center">
          <SvgIcon icon="mingcute:copper-coin-fill" class="text-[#ffcea4] text-2xl mr-0.5"></SvgIcon>
          <p class="text-[#fafafa]">普通积分：<span>{{ userBalance.model3Count || 0 }}</span>
            高级积分：<span>{{ userBalance.model4Count || 0 }}</span>
            绘画积分:<span>{{ userBalance.drawMjCount || 0 }}</span></p>
          <p class="flex ml-2 cursor-pointer select-none link text-[#f9f9f9]">
            <SvgIcon icon="material-symbols-light:info" class="text-[#ffcea4] text-xl mr-0.5"></SvgIcon>
            积分规则
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="less">

</style>
