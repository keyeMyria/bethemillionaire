from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views import View
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response

from account.models import UserProfile
from . import forms
from . import models

from lessons.models import Lesson
from account.models import UsiTechAccount, BitconnectAccount
from topic.models import StepControl, Note
from account import models as account_model

from . import serializers

from administration import models as admin_model


#step 1
class Step_1(View):
    template_name = 'topic/step_1.html'

    def get(self, request):
        steps = StepControl.objects.filter(short_name='step-1')

        models.StepCount.objects.update_or_create(user=request.user, defaults={'step1': True})

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='step-1-overview').count()
        total_subcomment = models.SubComment.objects.filter(topic='step-1-overview').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='step-1-overview').all()
        subcomments = models.SubComment.objects.filter(topic='step-1-overview').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'steps': steps,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        steps = StepControl.objects.filter(short_name='step-1')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'step-1-overview'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'step-1-overview'
                deploy1.save()

        if request.method == 'POST' and request.POST.get('step_2') == 'step_2':
            models.StepCount.objects.update_or_create(user=request.user, defaults={'step2': True})

            return redirect('topic:step_2')


        total_comment = models.Comment.objects.filter(topic='step-1-overview').count()
        total_subcomment = models.SubComment.objects.filter(topic='step-1-overview').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='step-1-overview').all()
        subcomments = models.SubComment.objects.filter(topic='step-1-overview').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'steps': steps,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)


#step 2
class Step_2(View):
    template_name = 'topic/step_2.html'

    def get(self, request):
        steps = StepControl.objects.filter(short_name='step-2')

        get_step = models.StepCount.objects.get(user=request.user)

        if not get_step.step2:
            return redirect('topic:step_1')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='step-2-setup-bitcoinwallet').count()
        total_subcomment = models.SubComment.objects.filter(topic='step-2-setup-bitcoinwallet').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='step-2-setup-bitcoinwallet').all()
        subcomments = models.SubComment.objects.filter(topic='step-2-setup-bitcoinwallet').all()

        ladger_nano_s_accounts = account_model.LedgerNanoSAccount.objects.get(user=request.user.sponsor)

        if ladger_nano_s_accounts.ledger_nano_s_username:
            ladger_nano_s_account = account_model.LedgerNanoSAccount.objects.get(user=request.user.sponsor)

        else:
            ladger_nano_s_account = account_model.LedgerNanoSAccount.objects.get(user__username='admin')


        coin_mama_accounts = account_model.CoinMamaAccount.objects.get(user=request.user.sponsor)

        if coin_mama_accounts.coin_mama_username:
            coin_mama_account = account_model.CoinMamaAccount.objects.get(user=request.user.sponsor)

        else:
            coin_mama_account = account_model.CoinMamaAccount.objects.get(user__username='admin')


        coin_base_accounts = account_model.CoinBaseAccount.objects.get(user=request.user.sponsor)

        if coin_base_accounts.coinbase_username:
            coin_base_account = account_model.CoinBaseAccount.objects.get(user=request.user.sponsor)

        else:
            coin_base_account = account_model.CoinBaseAccount.objects.get(user__username='admin')


        cex_io_accounts = account_model.CexIOAccount.objects.get(user=request.user.sponsor)

        if cex_io_accounts.cexio_username:
            cex_io_account = account_model.CexIOAccount.objects.get(user=request.user.sponsor)

        else:
            cex_io_account = account_model.CexIOAccount.objects.get(user__username='admin')


        bit_panda_accounts = account_model.BitPandaAccount.objects.get(user=request.user.sponsor)

        if bit_panda_accounts.bitpanda_username:
            bit_panda_account = account_model.BitPandaAccount.objects.get(user=request.user.sponsor)

        else:
            bit_panda_account = account_model.BitPandaAccount.objects.get(user__username='admin')


        inda_coin_accounts = account_model.IndaCoinAccount.objects.get(user=request.user.sponsor)

        if inda_coin_accounts.indacoin_username:
            inda_coin_account = account_model.IndaCoinAccount.objects.get(user=request.user.sponsor)

        else:
            inda_coin_account = account_model.IndaCoinAccount.objects.get(user__username='admin')


        local_bitcoin_accounts = account_model.LocalBitcoinsAccount.objects.get(user=request.user.sponsor)

        if local_bitcoin_accounts.local_bitcoins_username:
            local_bitcoin_account = account_model.LocalBitcoinsAccount.objects.get(user=request.user.sponsor)

        else:
            local_bitcoin_account = account_model.LocalBitcoinsAccount.objects.get(user__username='admin')



        trezors_accounts = account_model.TrezorSAccount.objects.get(user=request.user.sponsor)

        if trezors_accounts.trezor_username:
            trezors_account = account_model.TrezorSAccount.objects.get(user=request.user.sponsor)

        else:
            trezors_account = account_model.TrezorSAccount.objects.get(user__username='admin')



        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'steps': steps,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,

            'ladger_nano_s_account': ladger_nano_s_account,
            'coin_mama_account': coin_mama_account,
            'coin_base_account': coin_base_account,
            'cex_io_account': cex_io_account,
            'bit_panda_account': bit_panda_account,
            'inda_coin_account': inda_coin_account,
            'local_bitcoin_account': local_bitcoin_account,
            'trezors_account': trezors_account,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        steps = StepControl.objects.filter(short_name='step-2')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'step-2-setup-bitcoinwallet'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'step-2-setup-bitcoinwallet'
                deploy1.save()


        if request.method == 'POST' and request.POST.get('step_3') == 'step_3':
            models.StepCount.objects.update_or_create(user=request.user, defaults={'step3': True})

            return redirect('topic:step_3')


        total_comment = models.Comment.objects.filter(topic='step-2-setup-bitcoinwallet').count()
        total_subcomment = models.SubComment.objects.filter(topic='step-2-setup-bitcoinwallet').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='step-2-setup-bitcoinwallet').all()
        subcomments = models.SubComment.objects.filter(topic='step-2-setup-bitcoinwallet').all()

        ladger_nano_s_accounts = account_model.LedgerNanoSAccount.objects.get(user=request.user.sponsor)

        if ladger_nano_s_accounts.ledger_nano_s_username:
            ladger_nano_s_account = account_model.LedgerNanoSAccount.objects.get(user=request.user.sponsor)

        else:
            ladger_nano_s_account = account_model.LedgerNanoSAccount.objects.get(user__username='admin')


        coin_mama_accounts = account_model.CoinMamaAccount.objects.get(user=request.user.sponsor)

        if coin_mama_accounts.coin_mama_username:
            coin_mama_account = account_model.CoinMamaAccount.objects.get(user=request.user.sponsor)

        else:
            coin_mama_account = account_model.CoinMamaAccount.objects.get(user__username='admin')


        coin_base_accounts = account_model.CoinBaseAccount.objects.get(user=request.user.sponsor)

        if coin_base_accounts.coinbase_username:
            coin_base_account = account_model.CoinBaseAccount.objects.get(user=request.user.sponsor)

        else:
            coin_base_account = account_model.CoinBaseAccount.objects.get(user__username='admin')


        cex_io_accounts = account_model.CexIOAccount.objects.get(user=request.user.sponsor)

        if cex_io_accounts.cexio_username:
            cex_io_account = account_model.CexIOAccount.objects.get(user=request.user.sponsor)

        else:
            cex_io_account = account_model.CexIOAccount.objects.get(user__username='admin')


        bit_panda_accounts = account_model.BitPandaAccount.objects.get(user=request.user.sponsor)

        if bit_panda_accounts.bitpanda_username:
            bit_panda_account = account_model.BitPandaAccount.objects.get(user=request.user.sponsor)

        else:
            bit_panda_account = account_model.BitPandaAccount.objects.get(user__username='admin')


        inda_coin_accounts = account_model.IndaCoinAccount.objects.get(user=request.user.sponsor)

        if inda_coin_accounts.indacoin_username:
            inda_coin_account = account_model.IndaCoinAccount.objects.get(user=request.user.sponsor)

        else:
            inda_coin_account = account_model.IndaCoinAccount.objects.get(user__username='admin')


        local_bitcoin_accounts = account_model.LocalBitcoinsAccount.objects.get(user=request.user.sponsor)

        if local_bitcoin_accounts.local_bitcoins_username:
            local_bitcoin_account = account_model.LocalBitcoinsAccount.objects.get(user=request.user.sponsor)

        else:
            local_bitcoin_account = account_model.LocalBitcoinsAccount.objects.get(user__username='admin')


        trezors_accounts = account_model.TrezorSAccount.objects.get(user=request.user.sponsor)

        if trezors_accounts.trezor_username:
            trezors_account = account_model.TrezorSAccount.objects.get(user=request.user.sponsor)

        else:
            trezors_account = account_model.TrezorSAccount.objects.get(user__username='admin')



        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'steps': steps,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,

            'ladger_nano_s_account': ladger_nano_s_account,
            'coin_mama_account': coin_mama_account,
            'coin_base_account': coin_base_account,
            'cex_io_account': cex_io_account,
            'bit_panda_account': bit_panda_account,
            'inda_coin_account': inda_coin_account,
            'local_bitcoin_account': local_bitcoin_account,
            'trezors_account': trezors_account,
        }

        return render(request, self.template_name, variables)


#step 3
class Step_3(View):
    template_name = 'topic/step_3.html'

    def get(self, request):
        steps = StepControl.objects.filter(short_name='step-3')

        get_step = models.StepCount.objects.get(user=request.user)

        if not get_step.step3:
            return redirect('topic:step_2')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()


        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='step-3-wealth-vehicles').count()
        total_subcomment = models.SubComment.objects.filter(topic='step-3-wealth-vehicles').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='step-3-wealth-vehicles').all()
        subcomments = models.SubComment.objects.filter(topic='step-3-wealth-vehicles').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,

            'steps': steps,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        steps = StepControl.objects.filter(short_name='step-3')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        if request.method == 'POST' and request.POST.get('step_4') == 'step_4':
            models.StepCount.objects.update_or_create(user=request.user, defaults={'step4': True})

            return redirect('topic:step_4')


        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'step-3-wealth-vehicles'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'step-3-wealth-vehicles'
                deploy1.save()


        total_comment = models.Comment.objects.filter(topic='step-3-wealth-vehicles').count()
        total_subcomment = models.SubComment.objects.filter(topic='step-3-wealth-vehicles').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='step-3-wealth-vehicles').all()
        subcomments = models.SubComment.objects.filter(topic='step-3-wealth-vehicles').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,

            'steps': steps,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)



#step 4
class Step_4(View):
    template_name = 'topic/step_4.html'

    def get(self, request):
        steps = StepControl.objects.filter(short_name='step-4')

        get_step = models.StepCount.objects.get(user=request.user)

        if not get_step.step4:
            return redirect('topic:step_3')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='step-3-setup-multiple-passive-profile').count()
        total_subcomment = models.SubComment.objects.filter(topic='step-3-setup-multiple-passive-profile').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='step-3-setup-multiple-passive-profile').all()
        subcomments = models.SubComment.objects.filter(topic='step-3-setup-multiple-passive-profile').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'steps': steps,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        steps = StepControl.objects.filter(short_name='step-4')

        if request.method == 'POST' and request.POST.get('step_5') == 'step_5':
            models.StepCount.objects.update_or_create(user=request.user, defaults={'step5': True})

            return redirect('topic:step_5')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'step-3-setup-multiple-passive-profile'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'step-3-setup-multiple-passive-profile'
                deploy1.save()

        total_comment = models.Comment.objects.filter(topic='step-3-setup-multiple-passive-profile').count()
        total_subcomment = models.SubComment.objects.filter(topic='step-3-setup-multiple-passive-profile').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='step-3-setup-multiple-passive-profile').all()
        subcomments = models.SubComment.objects.filter(topic='step-3-setup-multiple-passive-profile').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'steps': steps,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)


#step 5
class Step_5(View):
    template_name = 'topic/step_5.html'

    def get(self, request):
        steps = StepControl.objects.filter(short_name='step-5')

        get_step = models.StepCount.objects.get(user=request.user)

        if not get_step.step5:
            return redirect('topic:step_4')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='step-5-start-promoting-btm').count()
        total_subcomment = models.SubComment.objects.filter(topic='step-5-start-promoting-btm').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='step-5-start-promoting-btm').all()
        subcomments = models.SubComment.objects.filter(topic='step-5-start-promoting-btm').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'steps': steps,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        steps = StepControl.objects.filter(short_name='step-5')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'step-5-start-promoting-btm'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'step-5-start-promoting-btm'
                deploy1.save()

        total_comment = models.Comment.objects.filter(topic='step-5-start-promoting-btm').count()
        total_subcomment = models.SubComment.objects.filter(topic='step-5-start-promoting-btm').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='step-5-start-promoting-btm').all()
        subcomments = models.SubComment.objects.filter(topic='step-5-start-promoting-btm').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'steps': steps,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)


##########Module start#########
#module - 1 :: lesson 1
class Lesson1(View):
    template_name = 'topic/lesson_1.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-1-lesson-1')

        videos = admin_model.VideoLink.objects.filter(lesson_name='m_1_l_1')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-1/')


        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-1-lesson-1')))
        except:
            noteForm = forms.NoteForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-1-lesson-1').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-1-lesson-1').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-1-lesson-1').all()
        subcomments = models.SubComment.objects.filter(topic='module-1-lesson-1').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,

            'videos': videos,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-1-lesson-1')

        videos = admin_model.VideoLink.objects.filter(lesson_name='m_1_l_1')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-1/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-1-lesson-1'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-1-lesson-1'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-1-lesson-1')

        total_comment = models.Comment.objects.filter(topic='module-1-lesson-1').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-1-lesson-1').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-1-lesson-1').all()
        subcomments = models.SubComment.objects.filter(topic='module-1-lesson-1').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,

            'videos': videos,
        }

        return render(request, self.template_name, variables)


#module - 1 :: lesson 2
class Lesson2(View):
    template_name = 'topic/lesson_2.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-1-lesson-2')

        videos = admin_model.VideoLink.objects.filter(lesson_name='m_1_l_2')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-1/')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-1-lesson-2')))
        except:
            noteForm = forms.NoteForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-1-lesson-2').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-1-lesson-2').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-1-lesson-2').all()
        subcomments = models.SubComment.objects.filter(topic='module-1-lesson-2').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,

            'videos': videos,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-1-lesson-2')

        videos = admin_model.VideoLink.objects.filter(lesson_name='m_1_l_2')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-1/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-1-lesson-2'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-1-lesson-2'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-1-lesson-2')

        total_comment = models.Comment.objects.filter(topic='module-1-lesson-2').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-1-lesson-2').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-1-lesson-2').all()
        subcomments = models.SubComment.objects.filter(topic='module-1-lesson-2').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,

            'videos': videos,
        }

        return render(request, self.template_name, variables)


#module - 2 :: lesson 1
class Module_2_Lesson_1(View):
    template_name = 'topic/module_2_lesson_1.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-2-lesson-1')

        videos = admin_model.VideoLink.objects.filter(lesson_name='m_2_l_1')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-2/')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-2-lesson-1')))
        except:
            noteForm = forms.NoteForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-2-lesson-1').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-2-lesson-1').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-2-lesson-1').all()
        subcomments = models.SubComment.objects.filter(topic='module-2-lesson-1').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,

            'videos': videos,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-2-lesson-1')

        videos = admin_model.VideoLink.objects.filter(lesson_name='m_2_l_1')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-2/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-2-lesson-1'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-2-lesson-1'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-2-lesson-1')

        total_comment = models.Comment.objects.filter(topic='module-2-lesson-1').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-2-lesson-1').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-2-lesson-1').all()
        subcomments = models.SubComment.objects.filter(topic='module-2-lesson-1').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,

            'videos': videos,
        }

        return render(request, self.template_name, variables)


#module - 2 :: lesson 2
class Module_2_Lesson_2(View):
    template_name = 'topic/module_2_lesson_2.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-2-lesson-2')

        videos = admin_model.VideoLink.objects.filter(lesson_name='m_2_l_2')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-2/')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-2-lesson-2')))
        except:
            noteForm = forms.NoteForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-2-lesson-2').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-2-lesson-2').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-2-lesson-2').all()
        subcomments = models.SubComment.objects.filter(topic='module-2-lesson-2').all()

        ladger_nano_s_accounts = account_model.LedgerNanoSAccount.objects.get(user=request.user.sponsor)

        if ladger_nano_s_accounts.ledger_nano_s_username:
            ladger_nano_s_account = account_model.LedgerNanoSAccount.objects.get(user=request.user.sponsor)

        else:
            ladger_nano_s_account = account_model.LedgerNanoSAccount.objects.get(user__username='admin')


        coin_base_accounts = account_model.CoinBaseAccount.objects.get(user=request.user.sponsor)

        if coin_base_accounts.coinbase_username:
            coin_base_account = account_model.CoinBaseAccount.objects.get(user=request.user.sponsor)

        else:
            coin_base_account = account_model.CoinBaseAccount.objects.get(user__username='admin')



        trezors_accounts = account_model.TrezorSAccount.objects.get(user=request.user.sponsor)

        if trezors_accounts.trezor_username:
            trezors_account = account_model.TrezorSAccount.objects.get(user=request.user.sponsor)

        else:
            trezors_account = account_model.TrezorSAccount.objects.get(user__username='admin')




        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,

            'videos': videos,

            'ladger_nano_s_account': ladger_nano_s_account,
            'coin_base_account': coin_base_account,
            'trezors_account': trezors_account,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-2-lesson-2')

        videos = admin_model.VideoLink.objects.filter(lesson_name='m_2_l_2')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-2/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-2-lesson-2'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-2-lesson-2'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-2-lesson-2')

        total_comment = models.Comment.objects.filter(topic='module-2-lesson-2').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-2-lesson-2').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-2-lesson-2').all()
        subcomments = models.SubComment.objects.filter(topic='module-2-lesson-2').all()

        ladger_nano_s_accounts = account_model.LedgerNanoSAccount.objects.get(user=request.user.sponsor)

        if ladger_nano_s_accounts.ledger_nano_s_username:
            ladger_nano_s_account = account_model.LedgerNanoSAccount.objects.get(user=request.user.sponsor)

        else:
            ladger_nano_s_account = account_model.LedgerNanoSAccount.objects.get(user__username='admin')


        coin_base_accounts = account_model.CoinBaseAccount.objects.get(user=request.user.sponsor)

        if coin_base_accounts.coinbase_username:
            coin_base_account = account_model.CoinBaseAccount.objects.get(user=request.user.sponsor)

        else:
            coin_base_account = account_model.CoinBaseAccount.objects.get(user__username='admin')


        trezors_accounts = account_model.TrezorSAccount.objects.get(user=request.user.sponsor)

        if trezors_accounts.trezor_username:
            trezors_account = account_model.TrezorSAccount.objects.get(user=request.user.sponsor)

        else:
            trezors_account = account_model.TrezorSAccount.objects.get(user__username='admin')




        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,

            'videos': videos,

            'ladger_nano_s_account': ladger_nano_s_account,
            'coin_base_account': coin_base_account,
            'trezors_account': trezors_account,
        }

        return render(request, self.template_name, variables)


#module - 2 :: lesson 3
class Module_2_Lesson_3(View):
    template_name = 'topic/module_2_lesson_3.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-2-lesson-3')

        videos = admin_model.VideoLink.objects.filter(lesson_name='m_2_l_3')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-2/')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-2-lesson-3')))
        except:
            noteForm = forms.NoteForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-2-lesson-3').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-2-lesson-3').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-2-lesson-3').all()
        subcomments = models.SubComment.objects.filter(topic='module-2-lesson-3').all()

        coin_mama_accounts = account_model.CoinMamaAccount.objects.get(user=request.user.sponsor)

        if coin_mama_accounts.coin_mama_username:
            coin_mama_account = account_model.CoinMamaAccount.objects.get(user=request.user.sponsor)

        else:
            coin_mama_account = account_model.CoinMamaAccount.objects.get(user__username='admin')


        coin_base_accounts = account_model.CoinBaseAccount.objects.get(user=request.user.sponsor)

        if coin_base_accounts.coinbase_username:
            coin_base_account = account_model.CoinBaseAccount.objects.get(user=request.user.sponsor)

        else:
            coin_base_account = account_model.CoinBaseAccount.objects.get(user__username='admin')


        cex_io_accounts = account_model.CexIOAccount.objects.get(user=request.user.sponsor)

        if cex_io_accounts.cexio_username:
            cex_io_account = account_model.CexIOAccount.objects.get(user=request.user.sponsor)

        else:
            cex_io_account = account_model.CexIOAccount.objects.get(user__username='admin')


        bit_panda_accounts = account_model.BitPandaAccount.objects.get(user=request.user.sponsor)

        if bit_panda_accounts.bitpanda_username:
            bit_panda_account = account_model.BitPandaAccount.objects.get(user=request.user.sponsor)

        else:
            bit_panda_account = account_model.BitPandaAccount.objects.get(user__username='admin')


        inda_coin_accounts = account_model.IndaCoinAccount.objects.get(user=request.user.sponsor)

        if inda_coin_accounts.indacoin_username:
            inda_coin_account = account_model.IndaCoinAccount.objects.get(user=request.user.sponsor)

        else:
            inda_coin_account = account_model.IndaCoinAccount.objects.get(user__username='admin')


        local_bitcoin_accounts = account_model.LocalBitcoinsAccount.objects.get(user=request.user.sponsor)

        if local_bitcoin_accounts.local_bitcoins_username:
            local_bitcoin_account = account_model.LocalBitcoinsAccount.objects.get(user=request.user.sponsor)

        else:
            local_bitcoin_account = account_model.LocalBitcoinsAccount.objects.get(user__username='admin')


        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,

            'videos': videos,

            'coin_mama_account': coin_mama_account,
            'coin_base_account': coin_base_account,
            'cex_io_account': cex_io_account,
            'bit_panda_account': bit_panda_account,
            'inda_coin_account': inda_coin_account,
            'local_bitcoin_account': local_bitcoin_account,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-2-lesson-3')

        videos = admin_model.VideoLink.objects.filter(lesson_name='m_2_l_3')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-2/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-2-lesson-3'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-2-lesson-3'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-2-lesson-3')

        total_comment = models.Comment.objects.filter(topic='module-2-lesson-3').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-2-lesson-3').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-2-lesson-3').all()
        subcomments = models.SubComment.objects.filter(topic='module-2-lesson-3').all()

        coin_mama_accounts = account_model.CoinMamaAccount.objects.get(user=request.user.sponsor)

        if coin_mama_accounts.coin_mama_username:
            coin_mama_account = account_model.CoinMamaAccount.objects.get(user=request.user.sponsor)

        else:
            coin_mama_account = account_model.CoinMamaAccount.objects.get(user__username='admin')


        coin_base_accounts = account_model.CoinBaseAccount.objects.get(user=request.user.sponsor)

        if coin_base_accounts.coinbase_username:
            coin_base_account = account_model.CoinBaseAccount.objects.get(user=request.user.sponsor)

        else:
            coin_base_account = account_model.CoinBaseAccount.objects.get(user__username='admin')


        cex_io_accounts = account_model.CexIOAccount.objects.get(user=request.user.sponsor)

        if cex_io_accounts.cexio_username:
            cex_io_account = account_model.CexIOAccount.objects.get(user=request.user.sponsor)

        else:
            cex_io_account = account_model.CexIOAccount.objects.get(user__username='admin')


        bit_panda_accounts = account_model.BitPandaAccount.objects.get(user=request.user.sponsor)

        if bit_panda_accounts.bitpanda_username:
            bit_panda_account = account_model.BitPandaAccount.objects.get(user=request.user.sponsor)

        else:
            bit_panda_account = account_model.BitPandaAccount.objects.get(user__username='admin')


        inda_coin_accounts = account_model.IndaCoinAccount.objects.get(user=request.user.sponsor)

        if inda_coin_accounts.indacoin_username:
            inda_coin_account = account_model.IndaCoinAccount.objects.get(user=request.user.sponsor)

        else:
            inda_coin_account = account_model.IndaCoinAccount.objects.get(user__username='admin')


        local_bitcoin_accounts = account_model.LocalBitcoinsAccount.objects.get(user=request.user.sponsor)

        if local_bitcoin_accounts.local_bitcoins_username:
            local_bitcoin_account = account_model.LocalBitcoinsAccount.objects.get(user=request.user.sponsor)

        else:
            local_bitcoin_account = account_model.LocalBitcoinsAccount.objects.get(user__username='admin')


        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,

            'videos': videos,

            'coin_mama_account': coin_mama_account,
            'coin_base_account': coin_base_account,
            'cex_io_account': cex_io_account,
            'bit_panda_account': bit_panda_account,
            'inda_coin_account': inda_coin_account,
            'local_bitcoin_account': local_bitcoin_account,
        }

        return render(request, self.template_name, variables)


#module - 2 :: lesson 4
class Module_2_Lesson_4(View):
    template_name = 'topic/module_2_lesson_4.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-2-lesson-4')

        videos = admin_model.VideoLink.objects.filter(lesson_name='m_2_l_4')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-2/')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-2-lesson-4')))
        except:
            noteForm = forms.NoteForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-2-lesson-4').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-2-lesson-4').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-2-lesson-4').all()
        subcomments = models.SubComment.objects.filter(topic='module-2-lesson-4').all()

        cryptocoin_accounts = account_model.CryptoPayCardAccount.objects.get(user=request.user.sponsor)

        if cryptocoin_accounts.cryptopay_card_username:
            cryptocoin_account = account_model.CryptoPayCardAccount.objects.get(user=request.user.sponsor)

        else:
            cryptocoin_account = account_model.CryptoPayCardAccount.objects.get(user__username='admin')


        spectrocoin_accounts = account_model.SpectroCoinCardAccount.objects.get(user=request.user.sponsor)

        if spectrocoin_accounts.spectrocoin_card_username:
            spectrocoin_account = account_model.SpectroCoinCardAccount.objects.get(user=request.user.sponsor)

        else:
            spectrocoin_account = account_model.SpectroCoinCardAccount.objects.get(user__username='admin')


        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,

            'videos': videos,

            'cryptocoin_account': cryptocoin_account,
            'spectrocoin_account': spectrocoin_account,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-2-lesson-4')

        videos = admin_model.VideoLink.objects.filter(lesson_name='m_2_l_4')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-2/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-2-lesson-4'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-2-lesson-4'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-2-lesson-4')

        total_comment = models.Comment.objects.filter(topic='module-2-lesson-4').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-2-lesson-4').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-2-lesson-4').all()
        subcomments = models.SubComment.objects.filter(topic='module-2-lesson-4').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,

            'videos': videos,
        }

        return render(request, self.template_name, variables)


#module - 3 :: lesson 1
class Module_3_Lesson_1(View):
    template_name = 'topic/module_3_lesson_1.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-3-lesson-1')

        videos = admin_model.VideoLink.objects.filter(lesson_name='m_3_l_1')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-3/')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-3-lesson-1')))
        except:
            noteForm = forms.NoteForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-3-lesson-1').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-3-lesson-1').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-3-lesson-1').all()
        subcomments = models.SubComment.objects.filter(topic='module-3-lesson-1').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,

            'videos': videos,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-3-lesson-1')

        videos = admin_model.VideoLink.objects.filter(lesson_name='m_3_l_1')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-3/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-3-lesson-1'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-3-lesson-1'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-3-lesson-1')

        total_comment = models.Comment.objects.filter(topic='module-3-lesson-1').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-3-lesson-1').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-3-lesson-1').all()
        subcomments = models.SubComment.objects.filter(topic='module-3-lesson-1').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,

            'videos': videos,
        }

        return render(request, self.template_name, variables)


#module - 3 :: lesson 2
class Module_3_Lesson_2(View):
    template_name = 'topic/module_3_lesson_2.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-3-lesson-2')

        videos = admin_model.VideoLink.objects.filter(lesson_name='m_3_l_2')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-3/')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-3-lesson-2')))
        except:
            noteForm = forms.NoteForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-3-lesson-2').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-3-lesson-2').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-3-lesson-2').all()
        subcomments = models.SubComment.objects.filter(topic='module-3-lesson-2').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,

            'videos': videos,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-3-lesson-2')

        videos = admin_model.VideoLink.objects.filter(lesson_name='m_3_l_2')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-3/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-3-lesson-2'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-3-lesson-2'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-3-lesson-2')

        total_comment = models.Comment.objects.filter(topic='module-3-lesson-2').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-3-lesson-2').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-3-lesson-2').all()
        subcomments = models.SubComment.objects.filter(topic='module-3-lesson-2').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,

            'videos': videos,
        }

        return render(request, self.template_name, variables)


#module - 3 :: lesson 3
class Module_3_Lesson_3(View):
    template_name = 'topic/module_3_lesson_3.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-3-lesson-3')

        videos = admin_model.VideoLink.objects.filter(lesson_name='m_3_l_3')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-3/')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-3-lesson-3')))
        except:
            noteForm = forms.NoteForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-3-lesson-3').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-3-lesson-3').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-3-lesson-3').all()
        subcomments = models.SubComment.objects.filter(topic='module-3-lesson-3').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,

            'videos': videos,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-3-lesson-3')

        videos = admin_model.VideoLink.objects.filter(lesson_name='m_3_l_3')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-3/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-3-lesson-3'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-3-lesson-3'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-3-lesson-3')

        total_comment = models.Comment.objects.filter(topic='module-3-lesson-3').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-3-lesson-3').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-3-lesson-3').all()
        subcomments = models.SubComment.objects.filter(topic='module-3-lesson-3').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,

            'videos': videos,
        }

        return render(request, self.template_name, variables)


#module - 4 :: lesson 1
class Module_4_Lesson_1(View):
    template_name = 'topic/module_4_lesson_1.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-4-lesson-1')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-4/')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()
        usiaccountForm = forms.UsiTechAccountForm(instance=UsiTechAccount.objects.get(user=request.user))

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-4-lesson-1')))
        except:
            noteForm = forms.NoteForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-4-lesson-1').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-4-lesson-1').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-4-lesson-1').all()
        subcomments = models.SubComment.objects.filter(topic='module-4-lesson-1').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'usiaccountForm': usiaccountForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-4-lesson-1')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-4/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)
        usiaccountForm = forms.UsiTechAccountForm(request.POST or None, instance=UsiTechAccount.objects.get(user=request.user))

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-4-lesson-1'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-4-lesson-1'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-4-lesson-1')

        if request.method == 'POST' and request.POST.get('usi_account') == 'usi_account':
            if usiaccountForm.is_valid():
                deploy = usiaccountForm.deploy(request)


        total_comment = models.Comment.objects.filter(topic='module-4-lesson-1').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-4-lesson-1').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-4-lesson-1').all()
        subcomments = models.SubComment.objects.filter(topic='module-4-lesson-1').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'usiaccountForm': usiaccountForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)


#module - 4 :: lesson 2
class Module_4_Lesson_2(View):
    template_name = 'topic/module_4_lesson_2.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-4-lesson-2')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-4/')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()
        bitconnectaccountForm = forms.BitconnectAccountForm(instance=BitconnectAccount.objects.get(user=request.user))

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-4-lesson-2')))
        except:
            noteForm = forms.NoteForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-4-lesson-2').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-4-lesson-2').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-4-lesson-2').all()
        subcomments = models.SubComment.objects.filter(topic='module-4-lesson-2').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'bitconnectaccountForm': bitconnectaccountForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-4-lesson-2')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-4/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)
        bitconnectaccountForm = forms.BitconnectAccountForm(request.POST or None, instance=BitconnectAccount.objects.get(user=request.user))

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-4-lesson-2'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-4-lesson-2'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-4-lesson-2')

        if request.method == 'POST' and request.POST.get('bitconnect_account') == 'bitconnect_account':
            if bitconnectaccountForm.is_valid():
                deploy = bitconnectaccountForm.deploy(request)


        total_comment = models.Comment.objects.filter(topic='module-4-lesson-2').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-4-lesson-2').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-4-lesson-2').all()
        subcomments = models.SubComment.objects.filter(topic='module-4-lesson-2').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'bitconnectaccountForm': bitconnectaccountForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)


#module - 4 :: lesson 3
class Module_4_Lesson_3(View):
    template_name = 'topic/module_4_lesson_3.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-4-lesson-3')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-4/')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-4-lesson-3')))
        except:
            noteForm = forms.NoteForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-4-lesson-3').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-4-lesson-3').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-4-lesson-3').all()
        subcomments = models.SubComment.objects.filter(topic='module-4-lesson-3').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-4-lesson-3')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-4/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-4-lesson-3'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-4-lesson-3'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-4-lesson-3')

        total_comment = models.Comment.objects.filter(topic='module-4-lesson-3').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-4-lesson-3').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-4-lesson-3').all()
        subcomments = models.SubComment.objects.filter(topic='module-4-lesson-3').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)


#module - 5 :: lesson 1
class Module_5_Lesson_1(View):
    template_name = 'topic/module_5_lesson_1.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-5-lesson-1')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-5/')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-5-lesson-1')))
        except:
            noteForm = forms.NoteForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-5-lesson-1').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-5-lesson-1').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-5-lesson-1').all()
        subcomments = models.SubComment.objects.filter(topic='module-5-lesson-1').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-5-lesson-1')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-5/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-5-lesson-1'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-5-lesson-1'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-5-lesson-1')

        total_comment = models.Comment.objects.filter(topic='module-5-lesson-1').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-5-lesson-1').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-5-lesson-1').all()
        subcomments = models.SubComment.objects.filter(topic='module-5-lesson-1').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)


#module - 5 :: lesson 2
class Module_5_Lesson_2(View):
    template_name = 'topic/module_5_lesson_2.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-5-lesson-2')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-5/')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-5-lesson-2')))
        except:
            noteForm = forms.NoteForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-5-lesson-2').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-5-lesson-2').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-5-lesson-2').all()
        subcomments = models.SubComment.objects.filter(topic='module-5-lesson-2').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-5-lesson-2')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-5/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-5-lesson-2'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-5-lesson-2'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-5-lesson-2')

        total_comment = models.Comment.objects.filter(topic='module-5-lesson-2').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-5-lesson-2').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-5-lesson-2').all()
        subcomments = models.SubComment.objects.filter(topic='module-5-lesson-2').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)


#module - 5 :: lesson 3
class Module_5_Lesson_3(View):
    template_name = 'topic/module_5_lesson_3.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-5-lesson-3')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-5/')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-5-lesson-3')))
        except:
            noteForm = forms.NoteForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-5-lesson-3').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-5-lesson-3').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-5-lesson-3').all()
        subcomments = models.SubComment.objects.filter(topic='module-5-lesson-3').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-5-lesson-3')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-5/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-5-lesson-3'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-5-lesson-3'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-5-lesson-3')

        total_comment = models.Comment.objects.filter(topic='module-5-lesson-3').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-5-lesson-3').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-5-lesson-3').all()
        subcomments = models.SubComment.objects.filter(topic='module-5-lesson-3').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)


#module - 5 :: lesson 4
class Module_5_Lesson_4(View):
    template_name = 'topic/module_5_lesson_4.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-5-lesson-4')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-5/')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-5-lesson-4')))
        except:
            noteForm = forms.NoteForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-5-lesson-4').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-5-lesson-4').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-5-lesson-4').all()
        subcomments = models.SubComment.objects.filter(topic='module-5-lesson-4').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-5-lesson-4')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-5/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-5-lesson-4'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-5-lesson-4'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-5-lesson-4')

        total_comment = models.Comment.objects.filter(topic='module-5-lesson-4').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-5-lesson-4').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-5-lesson-4').all()
        subcomments = models.SubComment.objects.filter(topic='module-5-lesson-4').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)


#module - 5 :: lesson 5
class Module_5_Lesson_5(View):
    template_name = 'topic/module_5_lesson_5.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-5-lesson-5')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-5/')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-5-lesson-5')))
        except:
            noteForm = forms.NoteForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-5-lesson-5').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-5-lesson-5').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-5-lesson-5').all()
        subcomments = models.SubComment.objects.filter(topic='module-5-lesson-5').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-5-lesson-5')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-5/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-5-lesson-5'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-5-lesson-5'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-5-lesson-5')

        total_comment = models.Comment.objects.filter(topic='module-5-lesson-5').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-5-lesson-5').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-5-lesson-5').all()
        subcomments = models.SubComment.objects.filter(topic='module-5-lesson-5').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)


#module - 5 :: lesson 6
class Module_5_Lesson_6(View):
    template_name = 'topic/module_5_lesson_6.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-5-lesson-6')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-5/')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-5-lesson-6')))
        except:
            noteForm = forms.NoteForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-5-lesson-6').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-5-lesson-6').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-5-lesson-6').all()
        subcomments = models.SubComment.objects.filter(topic='module-5-lesson-6').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-5-lesson-6')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-5/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-5-lesson-6'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-5-lesson-6'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-5-lesson-6')

        total_comment = models.Comment.objects.filter(topic='module-5-lesson-6').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-5-lesson-6').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-5-lesson-6').all()
        subcomments = models.SubComment.objects.filter(topic='module-5-lesson-6').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)


#module - 6 :: lesson 1
class Module_6_Lesson_1(View):
    template_name = 'topic/module_6_lesson_1.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-6-lesson-1')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-6/')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-6-lesson-1')))
        except:
            noteForm = forms.NoteForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-6-lesson-1').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-6-lesson-1').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-6-lesson-1').all()
        subcomments = models.SubComment.objects.filter(topic='module-6-lesson-1').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-6-lesson-1')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-6/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-6-lesson-1'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-6-lesson-1'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-6-lesson-1')

        total_comment = models.Comment.objects.filter(topic='module-6-lesson-1').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-6-lesson-1').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-6-lesson-1').all()
        subcomments = models.SubComment.objects.filter(topic='module-6-lesson-1').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)


#module - 6 :: lesson 2
class Module_6_Lesson_2(View):
    template_name = 'topic/module_6_lesson_2.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-6-lesson-2')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-6/')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-6-lesson-2')))
        except:
            noteForm = forms.NoteForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-6-lesson-2').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-6-lesson-2').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-6-lesson-2').all()
        subcomments = models.SubComment.objects.filter(topic='module-6-lesson-2').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-6-lesson-2')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-6/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-6-lesson-2'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-6-lesson-2'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-6-lesson-2')

        total_comment = models.Comment.objects.filter(topic='module-6-lesson-2').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-6-lesson-2').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-6-lesson-2').all()
        subcomments = models.SubComment.objects.filter(topic='module-6-lesson-2').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)


#module - 7 :: lesson 1
class Module_7_Lesson_1(View):
    template_name = 'topic/module_7_lesson_1.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-7-lesson-1')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-7/')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-7-lesson-1').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-7-lesson-1').count()

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-7-lesson-1')))
        except:
            noteForm = forms.NoteForm()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-7-lesson-1').all()
        subcomments = models.SubComment.objects.filter(topic='module-7-lesson-1').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-7-lesson-1')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-7/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-7-lesson-1'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-7-lesson-1'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-7-lesson-1')

        total_comment = models.Comment.objects.filter(topic='module-7-lesson-1').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-7-lesson-1').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-7-lesson-1').all()
        subcomments = models.SubComment.objects.filter(topic='module-7-lesson-1').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)


#module - 7 :: lesson 2
class Module_7_Lesson_2(View):
    template_name = 'topic/module_7_lesson_2.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-7-lesson-2')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-7/')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-7-lesson-2')))
        except:
            noteForm = forms.NoteForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-7-lesson-2').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-7-lesson-2').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-7-lesson-2').all()
        subcomments = models.SubComment.objects.filter(topic='module-7-lesson-2').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-7-lesson-2')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-7/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-7-lesson-2'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-7-lesson-2'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-7-lesson-2')

        total_comment = models.Comment.objects.filter(topic='module-7-lesson-2').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-7-lesson-2').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-7-lesson-2').all()
        subcomments = models.SubComment.objects.filter(topic='module-7-lesson-2').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)


#module - 7 :: lesson 3
class Module_7_Lesson_3(View):
    template_name = 'topic/module_7_lesson_3.html'

    def get(self, request):
        lessons = Lesson.objects.filter(short_name='module-7-lesson-3')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-7/')

        commentForm = forms.CommentForm()
        subcommentForm = forms.SubCommentForm()

        try:
            noteForm = forms.NoteForm(instance=Note.objects.get(Q(user=request.user) & Q(topic='module-7-lesson-3')))
        except:
            noteForm = forms.NoteForm()

        user_profile = UserProfile.objects.filter(username=request.user.username)

        total_comment = models.Comment.objects.filter(topic='module-7-lesson-3').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-7-lesson-3').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-7-lesson-3').all()
        subcomments = models.SubComment.objects.filter(topic='module-7-lesson-3').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        lessons = Lesson.objects.filter(short_name='module-7-lesson-3')

        for lesson in lessons:
            if not lesson.is_active:
                return HttpResponseRedirect('/lessons/module-7/')

        commentForm = forms.CommentForm(request.POST or None)
        subcommentForm = forms.SubCommentForm(request.POST or None)

        user_profile = UserProfile.objects.filter(username=request.user.username)

        if request.method == 'POST' and request.POST.get('comment_form') == 'comment_form':
            if commentForm.is_valid():
                deploy = commentForm.deploy(request)
                deploy.topic = 'module-7-lesson-3'
                deploy.save()


        if request.method == 'POST' and request.POST.get('subcomment_form') == 'subcomment_form':
            if subcommentForm.is_valid():
                comment_id = request.POST.get('commentid')
                print(comment_id)
                deploy1 = subcommentForm.deploy(request, comment_id)
                deploy1.topic = 'module-7-lesson-3'
                deploy1.save()

        noteForm = forms.NoteForm(request.POST or None)
        if request.method == 'POST' and request.POST.get('note_form') == 'note_form':
            if noteForm.is_valid():
                noteForm.deploy(request, 'module-7-lesson-3')

        total_comment = models.Comment.objects.filter(topic='module-7-lesson-3').count()
        total_subcomment = models.SubComment.objects.filter(topic='module-7-lesson-3').count()

        total_comments = total_comment + total_subcomment

        comments = models.Comment.objects.filter(topic='module-7-lesson-3').all()
        subcomments = models.SubComment.objects.filter(topic='module-7-lesson-3').all()

        variables = {
            'user_profile': user_profile,
            'commentForm': commentForm,
            'subcommentForm': subcommentForm,
            'noteForm': noteForm,
            'total_comments': total_comments,
            'comments': comments,
            'subcomments': subcomments,
        }

        return render(request, self.template_name, variables)






#==============================================================================================
#==============================================================================================
#                               api
#==============================================================================================
#==============================================================================================

class CommentAPI(APIView):

    def get(self, request):
        if request.GET.get("comment_id") and request.user.username == 'admin':

            comment_id = request.GET.get("comment_id")

            x = 'User authorized'

            if request.user.username == 'admin':

                commentObj = models.Comment.objects.get(id=comment_id)
                commentObj.delete()

                msg = 'Delete'
            else:
                x = 'Error authentication'
                msg = 'Not delete'

            return Response({
                'msg': msg,
                'x': x,
            })
        else:
            return Response({
                'x': 'not permitted to view',
            })




class SubCommentAPI(APIView):

    def get(self, request):
        if request.GET.get("subcomment_id") and request.user.username == 'admin':

            subcomment_id = request.GET.get("subcomment_id")

            x = 'User authorized'

            if request.user.username == 'admin':

                subcommentObj = models.SubComment.objects.get(id=subcomment_id)
                subcommentObj.delete()

                msg = 'Delete'
            else:
                x = 'Error authentication'
                msg = 'Not delete'

            return Response({
                'msg': msg,
                'x': x,
            })
        else:
            return Response({
                'x': 'not permitted to view',
            })
