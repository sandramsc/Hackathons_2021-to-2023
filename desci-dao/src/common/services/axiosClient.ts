import axios from 'axios';

const axiosClient = axios.create({
    baseURL: `${process.env.NEXT_PUBLIC_SERVER_URL}/api`
});

axiosClient.interceptors.response.use(
    function (response) {
        return response;
    },

);

export default axiosClient;