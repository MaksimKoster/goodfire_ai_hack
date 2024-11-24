PREAMBLE = """As an expert problem solver solve step by step the following mathematical questions."""

PROMPT = """
Q: The perimeter of a rectangle is 24 inches. What is the number of square inches in the maximum possible area for this rectangle?
A: Let one pair of parallel sides have length $x$ and the other pair of parallel sides have length $12-x$. This means that the perimeter of the rectangle is $x+x+12-x+12-x=24$ as the problem states. The area of this rectangle is $12x-x^2$. Completing the square results in $-(x-6)^2+36\\le 36$ since $(x-6)^2\\ge 0$, so the maximum area of $\\boxed{36}$ is obtained when the rectangle is a square of side length 6 inches.

Q: The Smith family has 4 sons and 3 daughters. In how many ways can they be seated in a row of 7 chairs such that at least 2 boys are next to each other?
A: This problem is a perfect candidate for complementary counting.  It will be fairly difficult to try to count this directly, since there are lots of possible cases (just two are BBBBGGG and BGGBBGB, where B is a boy and G is a girl).  But there is only one way to assign genders to the seating so that no two boys are next to each other, and that is BGBGBGB. If we seat the children as BGBGBGB, then there are $4!$ orderings for the 4 boys, and $3!$ orderings for the 3 girls, giving a total of $4! \\times 3! = 144$ seatings for the 7 children. These are the seatings that we don't want, so to count the seatings that we do want, we need to subtract these seatings from the total number of seatings without any restrictions.  Since there are 7 kids, there are $7!$ ways to seat them. So the answer is $7! - (4! \\times 3!) = 5040-144 = \\boxed{4896}$.

Q: A fly is on the edge of a ceiling of a circular room with a radius of 58 feet. The fly walks straight across the ceiling to the opposite edge, passing through the center of the circle. It then walks straight to another point on the edge of the circle but not back through the center. The third part of the journey is straight back to the original starting point. If the third part of the journey was 80 feet long, how many total feet did the fly travel over the course of all three parts?
A: The fly's journey traces out the three sides of triangle.  Because one side of this triangle is a diameter of the circular ceiling and the other two sides are chords of this circle, the triangle is a right triangle. If the radius of the circular room is 58 feet, then the diameter is $2 \\times 58 = 116$ feet. This is the hypotenuse of the right triangle. One of the legs is 80 feet, so the other leg must be equal to $\\sqrt{116^2 - 80^2} = \\sqrt{(13{,}456 - 6400)} = \\sqrt{7056} = 84$ feet. The total distance traveled by the fly is $116 + 84 + 80 = \\boxed{280}$ feet.

Q: Find the sum of all the integer solutions of  $x^4 - 25x^2 + 144 = 0$.
A: This quartic looks almost like a quadratic. We can turn it into one by making the substitution $y = x^2$, giving us $y^2 - 25y + 144 = 0$. We can factor this as $(y - 16)(y - 9) = 0$ to find that $y = 9$ or $y = 16$. We could also have used the quadratic formula to find this.\n\nNow, substituting $x^2$ back for $y$, we see that $x^2 = 9$ or $x^2 = 16$. It follows that the possible values for $x$ are $-3, 3, -4, 4$. Adding all of these values together, we find that the sum of all solutions is $\\boxed{0}$.

Q: What is the sum of the reciprocals of the natural-number factors of 6?
A: The natural-number factors of 6 are 1, 6, 2, 3. The sum of their reciprocals is $1/1+1/6+1/2+1/3=6/6+1/6+3/6+2/6=12/6=\\boxed{2}$.

Q: Four consecutive positive prime numbers have a sum that is divisible by three. What is the smallest possible value of this sum?
A: The smallest set of such prime numbers is $5,7,11,13$, making a sum of $\\boxed{36}$.

Q: Find $\\sec (-300^\\circ).$
A: We have that\n\\[\\sec (-300^\\circ) = \\frac{1}{\\cos (-300^\\circ)}.\\]Since the cosine function has period $360^\\circ,$\n\\[\\cos (-300^\\circ) = \\cos (-300^\\circ + 360^\\circ) = \\cos 60^\\circ = \\frac{1}{2},\\]so\n\\[\\frac{1}{\\cos (-300^\\circ)} = \\boxed{2}.\\]

Q: A translation of the plane takes $-3 + 2i$ to $-7 - i.$  Find the complex number that the translation takes $-4 + 5i$ to.
A: This translation takes $z$ to $z + w,$ where $w$ is a fixed complex number.  Thus,\n\\[-7 - i = (-3 + 2i) + w.\\]Hence, $w = -4 - 3i.$  Then the translation takes $-4 + 5i$ to $(-4 + 5i) + (-4 - 3i) = \\boxed{-8 + 2i}.$"""

PROMPT_SHORT = """
Q: The perimeter of a rectangle is 24 inches. What is the number of square inches in the maximum possible area for this rectangle?
A: Let one pair of parallel sides have length $x$ and the other pair of parallel sides have length $12-x$. This means that the perimeter of the rectangle is $x+x+12-x+12-x=24$ as the problem states. The area of this rectangle is $12x-x^2$. Completing the square results in $-(x-6)^2+36\\le 36$ since $(x-6)^2\\ge 0$, so the maximum area of $\\boxed{36}$ is obtained when the rectangle is a square of side length 6 inches.

Q: Find the sum of all the integer solutions of  $x^4 - 25x^2 + 144 = 0$.
A: This quartic looks almost like a quadratic. We can turn it into one by making the substitution $y = x^2$, giving us $y^2 - 25y + 144 = 0$. We can factor this as $(y - 16)(y - 9) = 0$ to find that $y = 9$ or $y = 16$. We could also have used the quadratic formula to find this.\n\nNow, substituting $x^2$ back for $y$, we see that $x^2 = 9$ or $x^2 = 16$. It follows that the possible values for $x$ are $-3, 3, -4, 4$. Adding all of these values together, we find that the sum of all solutions is $\\boxed{0}$.

Q: What is the sum of the reciprocals of the natural-number factors of 6?
A: The natural-number factors of 6 are 1, 6, 2, 3. The sum of their reciprocals is $1/1+1/6+1/2+1/3=6/6+1/6+3/6+2/6=12/6=\\boxed{2}$.

Q: Four consecutive positive prime numbers have a sum that is divisible by three. What is the smallest possible value of this sum?
A: The smallest set of such prime numbers is $5,7,11,13$, making a sum of $\\boxed{36}$.

Q: A translation of the plane takes $-3 + 2i$ to $-7 - i.$  Find the complex number that the translation takes $-4 + 5i$ to.
A: This translation takes $z$ to $z + w,$ where $w$ is a fixed complex number.  Thus,\n\\[-7 - i = (-3 + 2i) + w.\\]Hence, $w = -4 - 3i.$  Then the translation takes $-4 + 5i$ to $(-4 + 5i) + (-4 - 3i) = \\boxed{-8 + 2i}.$"""


TEMPLATE = """
Q: {question}
A:"""

ANS = """ 
Please provide the final answer to the following question, ensuring that the answer is wrapped in the \\boxed{}
"""

COMP_PROMT = """
You are Google Gemma, a Large Language Model (LLM) created by Google. You power an AI assistant designed to provide accurate and helpful information.
Your task is to compare two specific blocks of text enclosed in \boxed{SOME TEXT} from two different answers. If the blocks of text are equivalent in mathematical sense, write "Yes". If the blocks of text are different, write "No".
"""

COMP_TEMP = """
Answer 1: {correct_ans}
Answer 2: {model_ans}
"""