#Django
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
#Models
from .models import Profile
#Forms
from .forms import ProfileForm, ProfileUpdateForm


@login_required
def profile(request):
    """Vista para actializar el perfil del usuario"""
    if request.method == 'POST':
        user_form = ProfileForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Perfil actualizado exitosamente!')
            return redirect('profile')
        else:
            messages.error(request, "Error")
    else:
        user_form = ProfileForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        pro = Profile.objects.filter(user_id=request.user.id)
        if not pro:
            profile = Profile(user=request.user)
            profile.save()
    context = {
        'u_form': user_form,
        'p_form': profile_form
    }

    return render(request, 'user/profile.html', context)

@login_required
def password_change(request):
    """Vista para modificar la contraseña"""
    template_name = 'user/passwordChangeForm.html'
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Contraseña actualizada exitosamente!')
            return redirect('change')
    return render(request, template_name, {'form': form})
