def nth_term_of_geometric_series(firstTerm,ratio,n):
    if (not firstTerm) or (not ratio) or (not n):
        return "invalid input"
    term = (firstTerm) * ((ratio ) ** (n-1))
    return term

ans = nth_term_of_geometric_series(3,None,8)
print(ans)
ans = nth_term_of_geometric_series(3,2,8)
print(ans)