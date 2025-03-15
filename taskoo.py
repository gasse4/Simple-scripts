import numpy as np

rate = np.array([[3, 4, 0, 5 ,1],
                 [4, 0, 3, 4, 2],
                 [2, 5, 1, 0, 3]])
print(rate)

def cosine_similarity(user1, user2):
    filter = (user1 != 0) and (user2 != 0) 
    if sum(filter) == 0: 
        return 0
    u, v = user1[filter], user2[filter]
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

num_users = rate.shape[0]
similarity = np.zeros((num_users, num_users))

for i in range(num_users):
    for j in range(num_users):
        if i != j:
            similarity[i, j] = cosine_similarity(rate[i], rate[j])
            
def predict_rating(user_index, movie_index):
    similar_users = np.where(rate[:,movie_index] != 0)[0]
    if len(similar_users) == 0:
        return 0  
   
    num = 0
    den = 0
    for x in similar_users:
        num += similarity[user_index, x] * rate[x, movie_index]
        den += similarity[user_index, x]

    if den != 0:
        predicted_rating = num / den
    else:
        predicted_rating = 0
    print(predicted_rating)
