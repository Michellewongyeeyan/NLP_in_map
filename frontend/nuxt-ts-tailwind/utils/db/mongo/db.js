export async function apiMongo(url, options, local = false) {
  // 取得 url 資源 和 選項
  const BasisApiURL = "http://localhost:8001";
  try {
    // 請求
    const res = await fetch(`${BasisApiURL}/api/${url}`, options);
    const data = await res.json();
    return data;
  } catch (error) {
    // 如果 請求失敗（Server 死咗 ）
    return {
      error: "An error occurred.",
      code: 500,
      message: "Server Error.",
    };
  }
}
