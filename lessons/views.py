from django.shortcuts import render, HttpResponseRedirect
from django.views import View

from account.models import UserProfile
from topic import forms
from topic import models
from lessons.models import Module, Lesson

#module 1
class Module1(View):
    template_name = 'lessons/module-1_v_2.html'

    def get(self, request):
        modules = Module.objects.filter(short_name='module-1')
        lessons = Lesson.objects.filter(module__short_name='module-1')

        for module in modules:
            if not module.is_active:
                return HttpResponseRedirect('/course/how-to-grow-your-wealth-in-bitcoins/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        total_comment = models.Comment.objects.filter(topic='module-1').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-1').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-1').all()
        subcomments = models.SubComment.objects.filter(topic='module-1').all()

        variables = {
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'modules': modules,
            'lessons': lessons,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        modules = Module.objects.filter(short_name='module-1')
        lessons = Lesson.objects.filter(module__short_name='module-1')

        for module in modules:
            if not module.is_active:
                return HttpResponseRedirect('/course/how-to-grow-your-wealth-in-bitcoins/')


        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)


        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-1'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-1'
                deploy1.save()

        total_comment = models.Comment.objects.filter(topic='module-1').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-1').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-1').all()
        subcomments = models.SubComment.objects.filter(topic='module-1').all()

        variables = {
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'modules': modules,
            'lessons': lessons,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)


#module 2
class Module2(View):
    template_name = 'lessons/module-2_v_1.html'

    def get(self, request):
        modules = Module.objects.filter(short_name='module-2')
        lessons = Lesson.objects.filter(module__short_name='module-2')

        for module in modules:
            if not module.is_active:
                return HttpResponseRedirect('/course/how-to-grow-your-wealth-in-bitcoins/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        total_comment = models.Comment.objects.filter(topic='module-2').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-2').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-2').all()
        subcomments = models.SubComment.objects.filter(topic='module-2').all()

        variables = {
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'modules': modules,
            'lessons': lessons,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        modules = Module.objects.filter(short_name='module-2')
        lessons = Lesson.objects.filter(module__short_name='module-2')

        for module in modules:
            if not module.is_active:
                return HttpResponseRedirect('/course/how-to-grow-your-wealth-in-bitcoins/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-2'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-2'
                deploy1.save()

        total_comment = models.Comment.objects.filter(topic='module-2').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-2').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-2').all()
        subcomments = models.SubComment.objects.filter(topic='module-2').all()

        variables = {
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'modules': modules,
            'lessons': lessons,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)


#module 3
class Module3(View):
    template_name = 'lessons/module-3_v_1.html'

    def get(self, request):
        modules = Module.objects.filter(short_name='module-3')
        lessons = Lesson.objects.filter(module__short_name='module-3')

        for module in modules:
            if not module.is_active:
                return HttpResponseRedirect('/course/how-to-grow-your-wealth-in-bitcoins/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        total_comment = models.Comment.objects.filter(topic='module-3').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-3').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-3').all()
        subcomments = models.SubComment.objects.filter(topic='module-3').all()

        variables = {
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'modules': modules,
            'lessons': lessons,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        modules = Module.objects.filter(short_name='module-3')
        lessons = Lesson.objects.filter(module__short_name='module-3')

        for module in modules:
            if not module.is_active:
                return HttpResponseRedirect('/course/how-to-grow-your-wealth-in-bitcoins/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-3'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-3'
                deploy1.save()

        total_comment = models.Comment.objects.filter(topic='module-3').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-3').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-3').all()
        subcomments = models.SubComment.objects.filter(topic='module-3').all()

        variables = {
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'modules': modules,
            'lessons': lessons,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)


#module 4
class Module4(View):
    template_name = 'lessons/module-4.html'

    def get(self, request):
        modules = Module.objects.filter(short_name='module-4')
        lessons = Lesson.objects.filter(module__short_name='module-4')

        for module in modules:
            if not module.is_active:
                return HttpResponseRedirect('/course/how-to-grow-your-wealth-in-bitcoins/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-4').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-4').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-4').all()
        subcomments = models.SubComment.objects.filter(topic='module-4').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'modules': modules,
            'lessons': lessons,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        modules = Module.objects.filter(short_name='module-4')
        lessons = Lesson.objects.filter(module__short_name='module-4')

        for module in modules:
            if not module.is_active:
                return HttpResponseRedirect('/course/how-to-grow-your-wealth-in-bitcoins/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-4'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-4'
                deploy1.save()

        total_comment = models.Comment.objects.filter(topic='module-4').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-4').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-4').all()
        subcomments = models.SubComment.objects.filter(topic='module-4').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'modules': modules,
            'lessons': lessons,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)


#module 5
class Module5(View):
    template_name = 'lessons/module-5.html'

    def get(self, request):
        modules = Module.objects.filter(short_name='module-5')
        lessons = Lesson.objects.filter(module__short_name='module-5')

        for module in modules:
            if not module.is_active:
                return HttpResponseRedirect('/course/how-to-grow-your-wealth-in-bitcoins/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-5').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-5').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-5').all()
        subcomments = models.SubComment.objects.filter(topic='module-5').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'modules': modules,
            'lessons': lessons,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        modules = Module.objects.filter(short_name='module-5')
        lessons = Lesson.objects.filter(module__short_name='module-5')

        for module in modules:
            if not module.is_active:
                return HttpResponseRedirect('/course/how-to-grow-your-wealth-in-bitcoins/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-5'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-5'
                deploy1.save()

        total_comment = models.Comment.objects.filter(topic='module-5').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-5').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-5').all()
        subcomments = models.SubComment.objects.filter(topic='module-5').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'modules': modules,
            'lessons': lessons,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)


#module 6
class Module6(View):
    template_name = 'lessons/module-6.html'

    def get(self, request):
        modules = Module.objects.filter(short_name='module-6')
        lessons = Lesson.objects.filter(module__short_name='module-6')

        for module in modules:
            if not module.is_active:
                return HttpResponseRedirect('/course/how-to-grow-your-wealth-in-bitcoins/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-6').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-6').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-6').all()
        subcomments = models.SubComment.objects.filter(topic='module-6').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'modules': modules,
            'lessons': lessons,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        modules = Module.objects.filter(short_name='module-6')
        lessons = Lesson.objects.filter(module__short_name='module-6')

        for module in modules:
            if not module.is_active:
                return HttpResponseRedirect('/course/how-to-grow-your-wealth-in-bitcoins/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-6'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-6'
                deploy1.save()

        total_comment = models.Comment.objects.filter(topic='module-6').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-6').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-6').all()
        subcomments = models.SubComment.objects.filter(topic='module-6').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'modules': modules,
            'lessons': lessons,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)


#module 7
class Module7(View):
    template_name = 'lessons/module-7.html'

    def get(self, request):
        modules = Module.objects.filter(short_name='module-7')
        lessons = Lesson.objects.filter(module__short_name='module-7')

        for module in modules:
            if not module.is_active:
                return HttpResponseRedirect('/course/how-to-grow-your-wealth-in-bitcoins/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-7').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-7').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-7').all()
        subcomments = models.SubComment.objects.filter(topic='module-7').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'modules': modules,
            'lessons': lessons,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        modules = Module.objects.filter(short_name='module-7')
        lessons = Lesson.objects.filter(module__short_name='module-7')

        for module in modules:
            if not module.is_active:
                return HttpResponseRedirect('/course/how-to-grow-your-wealth-in-bitcoins/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-7'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-7'
                deploy1.save()

        total_comment = models.Comment.objects.filter(topic='module-7').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-7').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-7').all()
        subcomments = models.SubComment.objects.filter(topic='module-7').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'modules': modules,
            'lessons': lessons,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)
