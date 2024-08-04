import { apiMongo } from "~/utils/db/mongo/db";
import { getHeaders } from "~/utils/cookies.js";

export function getsChapterByNum(num) {
  const url = "chapter/data/" + num;
  const options = {
    method: "GET",
    headers: getHeaders(),
  };
  return apiMongo(url, options);
}
