#include <iostream>
#include <queue>

int main() {
    std::queue<int> queue;

    // 큐에 값 추가 (enqueue)
    queue.push(10);
    queue.push(20);
    queue.push(30);

    // 큐의 가장 앞의 값 출력 (front)하고 제거 (dequeue)
    std::cout << "Front element: " << queue.front() << std::endl; // 출력: 10
    queue.pop();

    std::cout << "Front element after pop: " << queue.front() << std::endl; // 출력: 20

    // 큐가 비어있는지 확인
    if (queue.empty()) {
        std::cout << "Queue is empty" << std::endl;
    } else {
        std::cout << "Queue is not empty" << std::endl;
    }

    return 0;
}
