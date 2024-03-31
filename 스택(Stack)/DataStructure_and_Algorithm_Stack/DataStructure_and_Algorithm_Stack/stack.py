# Python List로 스택 구현

# self는 파이썬에서 인스턴스 메서드에서 첫 번째 매개변수로 사용되는 관례적인 이름
# 이 매개변수는 현재 인스턴스를 가리키는 참조
# 파이썬에서 메서드를 호출할 때는 메서드가 속한 인스턴스를 자동으로 전달
# 일반적으로 클래스의 인스턴스 변수에 접근하거나 인스턴스 메서드를 호출할 때 self를 사용

class Stack():
    def __init__(self): # 클래스의 생성자 : 이 생성자는 스택을 초기화 함
        # self는 인스턴스 자체를 가리킴
        # 생성자가 호출될 때 이를 사용하여 클래스의 속성과 메서드에 액세스 할 수 있음
        self.stack = []
    
    def push(self,data):    # push함수 : stack에 데이터 추가
        self.stack.append(data)
    
    def pop(self):
        pop_object = None   # pop_object를 초기화
        # 스택이 비어 있는 경우에 pop()메서드를 호출했을 때, 실제로 스택에서 요소를 제거하고 반환할 수x
        # 이런 경우 pop() 메서드가 None을 반환하도록 한다.
        # 변수를 먼저 None으로 초기화 해놓고, 스택이 비어 있는지 여부를 확인한 후에 
        # 스택이 비어 있으면 pop_object의 값이 그대로 None이 유지되도록 한다.
        if self.isEmpty():
            print("Stack is Empty:(")
        else:
            pop_object = self.stack.pop()
        return pop_object
    
    def top(self):
        top_object = None
        if self.isEmpty():
            print("Stack is Empty:(")
        else:
            top_object = self.stack[-1]
        return top_object
    
    def isEmpty(self):
        is_empty = False    # 만약 스택이 비어있지 않다면 False 반환
        if len(self.stack) == 0:
            is_empty = True # 만약 스택이 비어있다면 True 반환
        return is_empty

def main():
    # Stack 객체 생성
    my_stack = Stack()

    # 스택에 데이터 추가
    print("Pushing elements onto the stack:")
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)

    # 스택에서 데이터 제거
    print("\nPopping elements from the stack:")
    while not my_stack.isEmpty():
        top_element = my_stack.pop()
        print("Popped:", top_element)

    # 더 이상 스택에 데이터가 없는 경우
    print("\nStack is now empty.")

if __name__ == "__main__":
    main()
