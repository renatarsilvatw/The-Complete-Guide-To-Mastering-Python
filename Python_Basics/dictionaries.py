users = {'user1': 'Mario123',
         'user2': 'Luigi456', 
         'items':{'apple':10,
                  'banana':20
                  }
        }
## users.clear();

# print(users['items']['apple'])

print(users.setdefault('user1', 'There is no key!'))
