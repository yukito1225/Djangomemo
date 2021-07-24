from .forms import PostForm, RecordNumberForm

def index(request, now_page=1):
    # レコード件数
    if 'record_number' in request.POST:
        record_number = request.POST['record_number']
    else: 
        record_number = 10

    record_number_form = RecordNumberForm()
    record_number_form.initial = {'record_number': str(record_number)}

    memos = Memo.objects.all()
    page = Paginator(memos, record_number)
    params = {
      'page': page.get_page(now_page),
      'form': PostForm(),
      'record_number_form': record_number_form,
    }
    return render(request, 'index.html', params)