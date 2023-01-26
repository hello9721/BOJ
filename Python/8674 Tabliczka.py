w, h = map(int, input().split())

if (w%2 == 0) | (h%2 == 0): print(0)
else:

    w_ = [w//2*h, (w//2+1)*h]
    h_ = [h//2*w, (h//2+1)*w]

    w_d = w_[1] - w_[0]
    h_d = h_[1] - h_[0]

    print(min(w_d, h_d))

