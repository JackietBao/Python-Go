<script setup lang='ts'>
import { computed, watch } from 'vue'
import { NLayout, NLayoutContent } from 'naive-ui'
import RightSider from './components/sider/index.vue'
import ChatBase from './chatBase.vue'
import { useBasicLayout } from '@/hooks/useBasicLayout'
import { useAppStore, useAuthStore, useChatStore } from '@/store'

const appStore = useAppStore()
const chatStore = useChatStore()
const authStore = useAuthStore()
const { isMobile } = useBasicLayout()
const isLogin = computed(() => authStore.isLogin)
const collapsed = computed(() => appStore.siderCollapsed)

watch(isLogin, async (newVal, oldVal) => {
  if (newVal && !oldVal)
    await chatStore.queryMyGroup()
})

const getMobileClass = computed(() => {
  if (isMobile.value)
    return ['rounded-none', 'shadow-none', ]
  return ['rounded-md', 'shadow-md', 'dark:border-neutral-800']
})

</script>

<template>
  <div class="h-full dark:bg-[#131323] transition-all"  >
    <div class="h-full overflow-hidden" :class="getMobileClass">

      <NLayout class="z-40 transition w-full h-full" :has-sider="true" sider-placement="left">

				<!-- 右侧侧对话页面 的侧边栏 -->
				<RightSider class="h-full"  />

        <!-- 聊天-->
        <ChatBase />

      </NLayout>
    </div>
  </div>
</template>
