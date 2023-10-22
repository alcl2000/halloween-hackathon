import axios from "axios";

axios.defaults.baseURL = "https://trick-or-trend-c24bf997221b.herokuapp.com/";
axios.defaults.headers.post["Content-Type"] = "multipart/form-data";
axios.defaults.withCredentials = true;

export const axiosReq = axios.create();
export const axiosRes = axios.create();