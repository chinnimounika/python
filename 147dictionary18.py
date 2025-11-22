#Converting list to dict
def convert_dict(a):
    init=iter(list1)
    res_dict=dict(zip(init,init))
    return res_dict
list1=['x',1,'y',2,'z',3]
print(convert_dict(list1))