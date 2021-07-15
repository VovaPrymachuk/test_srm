from django.contrib import messages
from django.shortcuts import render, redirect


class ObjectCreateMixin:
    model = None
    form_model = None
    template = None
    success_redirect_url = None
    error_redirect_url = None
    objects_already_create_error = None
    not_valid_form_message = None

    def get(self, request):
        form = self.form_model
        context = {'form': form}
        return render(request, self.template, context)

    def post(self, request):
        if self.model.__name__ == 'User':
            if self.model.objects.filter(username=request.POST['username']).exists():
                messages.error(request, self.objects_already_create_error)
                return redirect(self.error_redirect_url)
        else:
            if self.model.objects.filter(name=request.POST['name']).exists():
                messages.error(request, self.objects_already_create_error)
                return redirect(self.error_redirect_url)

        form = self.form_model(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, '{} created successfully'.format(self.model.__name__))
            return redirect(self.success_redirect_url)
        else:
            messages.error(request, self.not_valid_form_message)
            return redirect(self.error_redirect_url)


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None
    redirect_url = None

    def get(self, request, pk):
        object = self.model.objects.get(pk=pk)
        context = {
            'form': self.model_form(instance=object),
            self.model.__name__: object,
        }
        return render(request, self.template, context)

    def post(self, request, pk):
        object = self.model.objects.get(pk=pk)
        form = self.model_form(request.POST, instance=object)
        if form.is_valid():
            form.save()
            messages.success(
                request, '{} updated successfully'.format(self.model.__name__))
        else:
            messages.error(
                request, 'Error updating {}'.format(self.model.__name__))
        return redirect(self.redirect_url)


class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, pk):
        object = self.model.objects.get(pk=pk)
        context = {
            self.model.__name__: object
        }
        return render(request, self.template, context)

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        if self.model.__name__ == 'Group' and len(obj.user_set.all()) != 0:
            message = 'You cannot delete this group because it has users'
            messages.error(request, message)
        else:
            obj.delete()
            message = '{} deleted successfully'.format(self.model.__name__)
            messages.success(request, message)
        return redirect(self.redirect_url)
