from django.shortcuts import render

from collector.models import Company, Contact, Deal, Lead
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth


@main_auth(on_start=True, set_cookie=True)
def index(request):
    user_token = request.bitrix_user_token

    def process(class_to_process, name_field_name='TITLE'):
        for entry in user_token.call_list_method("crm." + class_to_process.__name__.lower() + ".list"):
            class_to_process.objects.update_or_create(id=int(entry['ID']), title=entry[name_field_name], data=entry)

    process(Company)
    process(Contact, name_field_name="NAME")
    process(Deal)
    process(Lead)

    return render(request, 'index.html')

