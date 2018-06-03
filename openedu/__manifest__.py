# -*- coding: utf-8 -*-
{
    'name': "OpenEdu",
    'author': "A4",
    'category': 'Education',
    'version': '0.1',
    'depends': ['base','openeducat_exam','openeducat_classroom'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/student_class_view.xml',
        'views/student_view.xml',
        'views/templates.xml',
        'views/classroom.xml',
        'demo/student_demo.xml',
        'demo/faculty_demo.xml',
        'demo/course_demo.xml',
        'demo/subject_demo.xml',
        'demo/classroom_demo.xml',
        'demo/batch_demo.xml',
        'demo/exam_type_demo.xml',
        'demo/res_partner_demo.xml',
        'demo/exam_session_demo.xml',
        'demo/exam_demo.xml',
        'demo/exam_attendees_demo.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}