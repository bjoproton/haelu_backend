from django.contrib import admin
from .models import Condition, Node, DecisionTree, DecisionTreeNodeM2M, DecisionTreeRuns
from decisions.decisiontreebuilder import DecisionTree as DTB
from django.utils.html import mark_safe

admin.site.register(Condition)
admin.site.register(Node)
#admin.site.register(DecisionTree)


class DecisionTreeNodeInline(admin.TabularInline):
    model = DecisionTreeNodeM2M


class DecisionTreeAdmin(admin.ModelAdmin):
    fields = ('name', 'plot')
    readonly_fields = ('plot', )
    inlines = [
        DecisionTreeNodeInline,
    ]

    @admin.display
    def plot(self, obj):
        content = DTB(obj).plot()
        return mark_safe(f'<img src="data:image/png;data:image/png;base64,{content}" alt="Decision Tree Plot" />')    


admin.site.register(DecisionTree, DecisionTreeAdmin)


admin.site.register(DecisionTreeRuns)
    
