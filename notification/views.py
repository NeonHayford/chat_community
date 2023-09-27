from django.shortcuts import render

# Create your views here.






# def send_file_email(request, file_id):
#     file = get_object_or_404(FileModels, pk=file_id)
#     if request.method == 'POST':
#         form = SendFileForm(request.POST)
#         if form.is_valid():
#             recipient_email = form.cleaned_data['recipient_email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             email= EmailMessage(
#                 subject, 
#                 message, 
#                 settings.EMAIL_HOST_USER, 
#                 [recipient_email], 
#                 reply_to=['another@example.com']
#                 )
#             email.attach_file(file.file.path)
#             email.send()
#             file.emails_sent += 1
#             file.save()
#             return redirect('filesystem:upload_list')
#     else:
#         form = SendFileForm()
#     return render(request, 'filesystem/send_file.html', {'form': form, 'file': file})
