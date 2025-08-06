# 用 Vite 建置 React 環境 (JavaScript)
PS-使用 create-react-app 指令 (官方已經不推薦使用這個了，所以就不再贅述了)

使用 Vite 建置 React 環境。
使用 vite 建置 React 的方法簡單一點，步驟是：

1. 使用 Vite 建立新的 React 專案: 在終端機中執行以下命令：
```bash
npm create vite@latest my-app --template react
```

2. 進入專案目錄：
```bash
cd my-app
```

3. 安裝相依性：
```bash
# 之前使用 node 20 建立專案
nvs use 20

npm install
```

4. 啟動開發伺服器：
```bash
npm run dev
```

到這邊就建置完成了，非常簡單吧！

文件檔案目錄結構
當你用 cli 快速建立出來專案後，新手可能會看到裡面有一堆資料夾，不知道從哪裡下手，這邊也簡單介紹一下每個目錄裡面是幹嘛的：
```bash
my-app/
├── node_modules/  # 套件資料夾
├── public/        # 靜態資源
├── src/           # 主要的 React 檔案
│   ├── App.js     # 主要的 React 組件
│   ├── index.js   # 程式進入點
│   ├── components/ # 可存放額外的組件
├── package.json   # 專案資訊與依賴
├── README.md      # 項目說明文件
└── ...
```

node_modules/：相關的依賴React 基礎概念
public/：存放靜態文件，例如 SVG、字體、圖片等等。
src/：你的主要工作區，像是自定義的 React 組件、程式邏輯都放在這裡。
package.json：專案的資訊和依賴的程式庫。
有時候我們也會新增 style/ 資料夾來放相關的樣式，或是 lib/ 資料夾放其他輔助的程式邏輯。

---

# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.
