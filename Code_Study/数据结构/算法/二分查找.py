def search(list_, key):             # 查
    low, high = 0, len(list_) - 1   # 变量作为决策的基础信息
    while low <= high:           # 分情况，反面情况优先
        mid = (low+high) // 2          
        if list_[mid] < key:
            low = mid + 1
        elif list_[mid] > key:
            high = mid - 1
        else:
            return mid

