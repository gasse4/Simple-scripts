def is_positive(sub):
    while True:
        if sub < 0:
            sub = int(input("Enter a positive value: "))
        else:
            break

sub1 = int(input("Enter the first score: "))
is_positive(sub1)
sub2 = int(input("Enter the second score: "))
is_positive(sub2)
sub3 = int(input("Enter the third score: "))
is_positive(sub3)

averege = (sub1+sub2+sub3)/3
print(f"The averege is: {averege:.4f}")
