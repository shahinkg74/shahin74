from course.models import Course

COURSE_CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(COURSE_CART_SESSION_ID)
        if not cart:
            cart = self.session[COURSE_CART_SESSION_ID] = {}
        self.cart = cart
    
    def __iter__(self):
        course_ids = self.cart.keys()   # get IDs courses -cart keys-
        courses = Course.objects.filter(id__in=course_ids)  # get the all courses in cart
        cart = self.cart.copy()
        for course in courses:
            cart[str(course.id)]['course'] = course    # add new item by name course -course name- in cart

        for value in cart.values():
            yield value     # return cart values

    def add(self, course):
        course_id = str(course.id)
        if course_id not in self.cart:
            self.cart[course_id] = {
                'quantity': 1,
                'price': str(course.price),
                'course_id': course_id
            }
            self.save()
    
    def total_price(self):
        return sum(int(value['price']) for value in self.cart.values())
    
    def remove(self, course):
        course_id = str(course.id)
        if course_id in self.cart:
            del self.cart[course_id]
            self.save()

    def clear(self):
        del self.session[COURSE_CART_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True
