from collections import deque
def solution(bridge_length, weight, truck_weights):
    # 조건. 트럭은 최대 bridge_legth 만큼 올라갈 수있다
    # 조건. 다리는 weight 이하까지 무게 견딜수 있다
    
    time = 0
    # 다리 개수만큼 
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    current_weight = 0
    while truck_weights:
        time +=1
        current_weight -= bridge.popleft()
        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                truck_on_bridge = truck_weights.popleft()
                bridge.append(truck_on_bridge)
                current_weight += truck_on_bridge
            else:
                bridge.append(0)
    time = time + bridge_length
    return time