#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> targets) {
    int answer = 0, idx = 0;
    
    // 타겟의 end 값을 기준으로 오름차순 정렬
    sort(targets.begin(), targets.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1];
    });
    
    while (idx < targets.size()) {
        // 현재 타겟의 end 값을 기준으로 요격 시스템 설정
        int end = targets[idx++][1];
        answer++;
        
        // 겹치는 타겟들을 모두 건너뜀
        while (idx < targets.size() && targets[idx][0] < end) {
            idx++;
        }
    }
    
    return answer;
}
