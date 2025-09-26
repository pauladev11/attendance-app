import datetime
from django.core.exceptions import ObjectDoesNotExist

def week_range(date):
    """Find the first/last day of the week for the given day.
    Assuming weeks start on Sunday and end on Saturday.
    Returns a tuple of ``(start_date, end_date)``.

    """
    # isocalendar calculates the year, week of the year, and day of the week.
    # dow is Mon = 1, Sat = 6, Sun = 7
    year, week, dow = date.isocalendar()

    # Find the first day of the week.
    if dow == 7:
        # Since we want to start with Sunday, let's test for that condition.
        start_date = date
    else:
        # Otherwise, subtract `dow` number days to get the first day
        start_date = date - datetime.timedelta(dow)

    # Now, add 6 for the last day of the week (i.e., count up to Saturday)
    end_date = start_date + datetime.timedelta(6)

    return (start_date, end_date)

def date_to_str(date_obj):
    return date_obj.strftime('%b %d, %Y')

def get_source_list(source):
    if not source or source == 'all':
        res = ['trade', 'farm']
    else:
        res = [source]
    return res

def get_object_or_None(model, arg):
    try:
        res  = model.objects.get(id=arg)
    except ObjectDoesNotExist:
        res = None
    return res
    