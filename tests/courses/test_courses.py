from models.create_course import CreateCourse


class TestCourse:
    def test_course_add(self, app, auth):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page added course
        5. Fill him a random data
        6. Add a new course
        """
        app.admin.add_new_course()
        course_data = CreateCourse.random()
        app.course.create_course(course_data)
        assert (app.course.new_course_page() == course_data.full_course_name), \
            "The course was not created!"

    def test_course_delete(self, app, auth):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page added course
        5. Fill him a random data
        6. Add a new course
        7. Delete course
        """
        app.admin.add_new_course()
        course_data = CreateCourse.random()
        app.course.create_course(course_data)
        app.admin.manage_courses()
        app.course.delete_course()
        assert (course_data.short_course_name in app.course.sure_delete()), \
            "The course was not deleted!"
