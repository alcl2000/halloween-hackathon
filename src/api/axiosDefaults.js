import axios from "axios";

axios.defaults.baseURL = "https://trick-or-treat-drf-api-09114a4f424d.herokuapp.com/";
axios.defaults.headers.post["Content-Type"] = "multipart/form-data";
axios.defaults.withCredentials = true;

export const axiosReq = axios.create();
export const axiosRes = axios.create();