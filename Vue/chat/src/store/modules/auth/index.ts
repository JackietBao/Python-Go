import {defineStore} from 'pinia'
import {useChatStore} from '../chat'
import type {AuthState, GlobalConfig, UserBalance} from './helper'
import {getToken, MjDrawFormConfig, removeToken, setToken} from './helper'
import {store} from '@/store'
import {fetchGetInfo} from '@/api'
import {fetchQueryConfigAPI} from '@/api/config'
import {fetchGetBalanceQueryAPI} from '@/api/balance'
import type {ResData} from '@/api/types'
import {checkAuth} from "@/api/global";
import {fetchGetRemix} from "@/api/mjDraw";

export const useAuthStore = defineStore('auth-store', {
    state: (): AuthState => ({
        token: getToken(),
        inspirationDialog: false, // remix
        openRemixModal: false, // remix
        previewDrawDialog: false, // 局部重绘
        customZoomDialog: false, // 自定义缩放
        previewDrawTaskId: 0, // 预览的任务ID
        sendSquareDialog: false, // 发送灵感广场
        sendSquareTaskId: 0, // 发送灵感广场的图片ID
        loginDialog: false,
        globalConfigLoading: true,
        userInfo: {},
        userBalance: {},
        globalConfig: {} as GlobalConfig,
        loadInit: false,
        isGenuine: 0, // 是否正版.
        drawId: '',
        taskId: '',
        mjDrawForm: {
            prompt: "", // 绘画内容
            model: 'MJ-5.2', // 模型版本
            style: '', // 风格
            quality: '2', // 质量
            stylize: 100, // 风格化 1-1000 <p>值越小越可靠、默认0最为精准</p>
            diversity: 30, // 多样性 0-1000    <p>混乱级别，可以理解为让AI天马行空的空间</p>
            similarity: '1', // 相似度
            sensitiveWords: '', // 敏感词
            size: '9:16',
            baseImage: [],
            mode: 1,  // 模式 1 fast 快速模式  2 relax  休闲模式  3 turbo
            translate: 1, // 翻译
            extendParam: []
        } as MjDrawFormConfig
    }),

    getters: {
        isLogin: (state: AuthState) => !!state.token,
        mjMode: (state: AuthState) => state.mjDrawForm.mode,
        mjTranslate: (state: AuthState) => state.mjDrawForm.translate,
        prompt: (state: AuthState) => state.mjDrawForm.prompt,
    },

    actions: {

        // 提取公共的功能
        checkAuth(){
            if(!this.token) {
                this.setLoginDialog(true);
                return false
            }
            return true
        },

        async getUserInfo(): Promise<T> {
            try {
                if (!this.loadInit)
                    await this.getglobalConfig()

                const res: { data: { userInfo: any, userBalance: any } } | void = await fetchGetInfo()
                if (!res)
                    return Promise.resolve(res)
                const {data} = res;
                const {userInfo, userBalance} = data
                this.userInfo = {...userInfo}
                this.userBalance = {...userBalance}
                return Promise.resolve(data)
            } catch (error) {
                return Promise.reject(error)
            }
        },

        updateUserBanance(userBalance: UserBalance) {
            this.userBalance = userBalance
        },

        updateInspireDialog(show: boolean) {
            this.inspirationDialog = show
        },

        updateDrawId(param: { id: string }) {
            this.drawId = param.id
        },
        updateCustomZoom(show: boolean, taskId: string) {
            this.customZoomDialog = show;
            this.taskId = taskId;
        },

				async updateRemixModal(mode: boolean, data?: {
					customId: string;
					prompt: string;
					taskId: string;
				}) {
							this.openRemixModal = mode
							if (data) {
								this.openRemixModalData = data;
							}
							// this.openRemixModal = await fetchGetRemix({mode}).then(res => res.data);
				},

        // 预览
        updatePreview(show:boolean, param: number) {
            this.previewDrawDialog = show
            this.previewDrawTaskId = param
        },

        // 更新
        updateMjChatConfig(param: { mode: number, translate: number }) {
            const {mode, translate} = param;
            this.mjDrawForm.mode = mode
            this.mjDrawForm.translate = translate
        },

        updateMjDrawForm(form: MjDrawFormConfig) {
            this.mjDrawForm = form
        },

        // 更新描述词
        updatePromptWords(form: { prompt: string }) {
            this.mjDrawForm.prompt = form.prompt
        },

        // 更新描述词
        updateMjDrawList(form) {
            this.mjDrawForm.prompt = form.prompt
        },

        // 更新发送到灵感广场
        updateSendSquire(show: boolean, param: number) {

            this.sendSquareDialog = show;
            if (show) {
                this.sendSquareTaskId = param;
            }

        },

        async getUserBalance() {
            const res: ResData = await fetchGetBalanceQueryAPI()
            const {success, data} = res
            if (success)
                this.userBalance = data
        },

        async getGoMaxAiAuth(domain: string) {
            const res: ResData = await checkAuth({domain})

            const {success, data} = res
            if (success)
                this.isGenuine = !data ? 1 : 2
        },

        async getglobalConfig(domain = '') {
            const res = await fetchQueryConfigAPI({domain})
            this.globalConfig = res.data
            this.globalConfigLoading = false
            this.loadInit = true
        },

        setToken(token: string) {
            this.token = token
            setToken(token)
        },

        removeToken() {
            this.token = undefined
            removeToken()
        },

        setLoginDialog(bool: boolean) {
            this.loginDialog = bool
        },

        logOut() {
            this.token = undefined
            removeToken()
            this.userInfo = {}
            this.userBalance = {}
            window.$message.success('登出账户成功！')
            const chatStore = useChatStore()
            chatStore.clearChat()
        },

        updatePasswordSuccess() {
            this.token = undefined
            removeToken()
            this.userInfo = {}
            this.userBalance = {}
            this.loginDialog = true
        },


    },
})

export function useAuthStoreWithout() {
    return useAuthStore(store)
}
