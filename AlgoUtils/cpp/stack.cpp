#include <iostream>
#include <stack>

int main() {
    std::stack<int> stack;

    // 스택에 값 추가 (push)
    stack.push(10);
    stack.push(20);
    stack.push(30);

    // 스택의 최상단 값을 출력하고 제거 (pop)
    std::cout << "Top element: " << stack.top() << std::endl; // 출력: 30
    stack.pop();

    std::cout << "Top element after pop: " << stack.top() << std::endl; // 출력: 20

    // 스택이 비어있는지 확인
    if (stack.empty()) {
        std::cout << "Stack is empty" << std::endl;
    } else {
        std::cout << "Stack is not empty" << std::endl;
    }

    return 0;
}
