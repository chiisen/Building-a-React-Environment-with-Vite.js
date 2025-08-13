import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'


import { useTranslation } from 'react-i18next';
import { i18nKeys } from './locales/i18nKeys'


import i18n from './locales/i18n';


function App() {
  const [count, setCount] = useState(0)


  const { t } = useTranslation();


  const [menuOpen, setMenuOpen] = useState(false);
  // 語言切換處理
  const [lang, setLang] = useState(i18n.language || 'en');
  const handleLangChange = (e) => {
    const newLang = e.target.value;
    setLang(newLang);
    i18n.changeLanguage(newLang);
    if (typeof window !== 'undefined') {
      localStorage.setItem('i18nLang', newLang);
    }
  };

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          {t(i18nKeys.HomePage_Count_Text)} {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        {t(i18nKeys.HomePage_Click_Text)}
      </p>

      <div className="navbar-left">
        <div className="hamburger" onClick={() => setMenuOpen(!menuOpen)}>☰</div>
        <div className={`navbar-links ${menuOpen ? 'open' : ''} navbar-links-flex`}>
        </div>
      </div>
      {/* 語言切換下拉選單靠右 */}
      <select
        className="lang-select"
        value={lang}
        onChange={handleLangChange}
      >
        <option value="en">English</option>
        <option value="zh_tw">繁體中文</option>
      </select>
    </>
  )
}

export default App
