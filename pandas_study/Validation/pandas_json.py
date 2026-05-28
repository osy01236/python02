import pandas as pd
import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches

with open("012_000000.json",'r', encoding='utf-8') as f:
    data=json.load(f)

annotations = [
    a for a in data['annotations']
    if "category_name" in a
]
#데이터 프레임으로 저장하기
df = pd.DataFrame(annotations)
counts = df['category_name'].value_counts()
print("트럭 : ", counts["truck"])

#차량들의 너비 값 출력
car_width = df["bbox"]
print(car_width)

#문제 너비가 가장 큰 차량을  찾으시오, 이미지에 바운딩 박스 표시하기
car_max_width = df[df["category_name"] == "car"].copy()

car_width = car_max_width["bbox"].apply(lambda x: x[1][0])
max_width = car_width.max()

# 가장 너비가 큰 차량의 행 찾기
max_car = car_max_width[car_width == max_width].iloc[0]

# bbox 값 꺼내기
x = max_car["bbox"][0][0]
y = max_car["bbox"][0][1]
w = max_car["bbox"][1][0]
h = max_car["bbox"][1][1]

img = plt.imread("012_000000.jpg")
plt.imshow(img)

ax= plt.gca()

# 바운딩 박스 그리기
rect = patches.Rectangle(
    (x, y),
    w,
    h,
    edgecolor="red",
    facecolor="none",
    linewidth=3
)

ax.add_patch(rect)

plt.axis("off")
plt.show()




#문제 각차량별 너비를 구하여 그래프로 출력해보세요
car_df = df[df["category_name"] == "car"].copy()

car_width = car_df["bbox"].apply(lambda x: x[1][0])

plt.figure(figsize=(10, 5))
plt.bar(range(1, len(car_width) + 1), car_width)

plt.title("Car Width")
plt.xlabel("Car")
plt.ylabel("Width")
plt.xticks(range(1, len(car_width) + 1))

plt.show()