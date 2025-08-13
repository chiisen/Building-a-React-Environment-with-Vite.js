import { initReactI18next } from 'react-i18next'
import i18n from 'i18next'


import en_us from './en-us.json'
import zh_tw from './zh-tw.json'

export const resources = {
  en_us: {
    translation: en_us,
  },
  zh_tw: {
    translation: zh_tw,
  },
}


// 讀取 localStorage 的語言設定
const savedLang = typeof window !== 'undefined' ? localStorage.getItem('i18nLang') : null;

i18n
  .use(initReactI18next)
  .init({
    resources,
    fallbackLng: {
      'en-*': ['en_us'],
      'en': ['en_us'],
      'zh-TW': ['zh_tw'],
      'zh-HK': ['zh_tw'],
      'zh-MO': ['zh_tw'],
      'zh': ['zh_tw'],
      'default': ['en_us']
    },
    lng: savedLang || 'en_us', // 優先用 localStorage
  })

export default i18n