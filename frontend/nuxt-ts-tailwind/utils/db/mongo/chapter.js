import { apiMongo } from "~/utils/db/mongo/db";
import { getCookie } from "~/utils/cookies.js";

export function getHeaders() {
  return {
    Accept: "application/json",
    "Content-Type": "application/json",
    Authorization: `Bearer ${getCookie("token")}`,
  };
}

export function getsChapterByNum(num) {
  const url = "chapter/data/" + num;
  const options = {
    method: "GET",
    headers: getHeaders(),
  };
  return apiMongo(url, options);
}
