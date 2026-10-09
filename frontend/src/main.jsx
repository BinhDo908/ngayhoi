import { StrictMode, useState } from "react"
import { createRoot } from "react-dom/client"
import "./style.css"

const apiUrl = "http://localhost:8000/api/dang-ky"

function App() {
  const [maSv, setMaSv] = useState("")
  const [maPhien, setMaPhien] = useState("")
  const [ketQua, setKetQua] = useState(null)
  const [dangGui, setDangGui] = useState(false)

  async function guiDangKy(event) {
    event.preventDefault()
    setDangGui(true)
    setKetQua(null)

    try {
      const response = await fetch(apiUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ma_sv: maSv, ma_phien: maPhien })
      })
      const data = await response.json()
      setKetQua({ status: response.status, data })
    } catch {
      setKetQua({ status: 0, data: { detail: "Không thể kết nối tới máy chủ." } })
    } finally {
      setDangGui(false)
    }
  }

  const trangThai = {
    201: { title: "Đăng ký thành công", message: "Thông tin của bạn đã được ghi nhận.", tone: "success" },
    409: { title: "Đã đăng ký", message: "Bạn đã đăng ký phiên học này trước đó.", tone: "warning" },
    422: { title: "Thông tin chưa hợp lệ", message: "Vui lòng nhập đầy đủ mã sinh viên và mã phiên.", tone: "error" },
    0: { title: "Không kết nối được máy chủ", message: "Hãy kiểm tra FastAPI đang chạy tại cổng 8000.", tone: "error" }
  }[ketQua?.status]

  return (
    <main className="page">
      <section className="card">
        <div className="badge">CSE3051 · BUỔI 3</div>
        <h1>Đăng ký phiên học</h1>
        <p className="intro">Nhập thông tin để xác nhận tham gia phiên học.</p>
        <form onSubmit={guiDangKy}>
          <label htmlFor="ma-sv">Mã sinh viên</label>
          <input id="ma-sv" value={maSv} onChange={(event) => setMaSv(event.target.value)} />
          <label htmlFor="ma-phien">Mã phiên</label>
          <input id="ma-phien" value={maPhien} onChange={(event) => setMaPhien(event.target.value)} />
          <button type="submit" disabled={dangGui}>{dangGui ? "Đang gửi..." : "Đăng ký"}</button>
        </form>
        {trangThai && (
          <div className={`result ${trangThai.tone}`} role="status">
            <span className="code">{ketQua.status}</span>
            <div>
              <strong>{trangThai.title}</strong>
              <p>{trangThai.message}</p>
            </div>
          </div>
        )}
      </section>
    </main>
  )
}

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <App />
  </StrictMode>
)
