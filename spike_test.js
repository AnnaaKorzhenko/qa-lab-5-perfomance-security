import http from 'k6/http';
import { sleep, check } from 'k6';

// кількість користувачів з консолі (якщо нема, дефолт 100)
const TARGET_VUS = __ENV.VUS ? parseInt(__ENV.VUS) : 100;

export const options = {
    stages: [
        { duration: '10s', target: 10 },
        { duration: '5s', target: TARGET_VUS },  // спайк
        { duration: '20s', target: TARGET_VUS },
        { duration: '10s', target: 10 },
        { duration: '10s', target: 0 },
    ],
    thresholds: {
        http_req_duration: ['p(95)<2000'],
        http_req_failed: ['rate<0.05'],
    },
};

export default function () {
    const res = http.get('http://localhost:3000/rest/products/search?q=apple');

    check(res, {
        'status is 200': (r) => r.status === 200,
    });

    sleep(1);
}