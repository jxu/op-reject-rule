# Simple modification of Kadane's algorithm too slow


def S(n, l):
    A = [0] * n
    m = [0] * n  # Kadane's algorithm partials
    M = [0] * (l+1)
    jd = [0] * (l+1)

    # pre-compute Tribonacci numbers
    t = [0] * 2*l
    t[2] = 1
    for k in range(3, 2*l):
        t[k] = (t[k-1] + t[k-2] + t[k-3]) % n

    for i in range(1, l+1):
        j = t[2*i-2] % n
        A[j] += 2*(t[2*i-1] % n) - n + 1

        while j < n:
            old_mj = m[j]
            if j == 0:
                m[j] = max(0, A[0])
            else:
                m[j] = max(m[j-1] + A[j], A[j])

            if m[j] == old_mj: break

            j += 1
            jd[i] += 1

        M[i] = max(m)

        print(A, m, M[i])

    print(M)
    print(jd, sum(jd) / len(jd))
    return M





print(sum(S(14, 100)))




