#include <cmath>
#include <algorithm>

using namespace std;

long long solution(int r1, int r2) {
    long long answer = 0;

    // 각 x에 대해 가능한 y의 범위를 계산
    for (int x = 1; x <= r2; x++) {
        // r2 원의 경계에서의 y 최대값
        long long y_max = floor(sqrt((long long)r2 * r2 - (long long)x * x));
        // r1 원의 경계에서의 y 최소값 (r1보다 큰 부분만 포함해야 하므로)
        long long y_min = ceil(sqrt((long long)r1 * r1 - (long long)x * x));

        // y_min이 0보다 작은 경우 (y_min이 계산되지 않는 경우 포함)
        if (r1 > x) y_min = max(0LL, y_min);

        // 두 원 사이의 y 값들의 개수를 더함
        answer += (y_max - y_min + 1);
    }
    
    // y = 0 축을 중심으로 한 대칭으로 인해 두 배
    return answer * 4;
}
