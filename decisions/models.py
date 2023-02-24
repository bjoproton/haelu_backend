# General imports
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Haelu imports
from haelu.enums import VALUE_TYPE_CHOICES, VALUE_TYPE_BOOLEAN, OPERATOR_CHOICES, OPERATOR_EQUAL_TO
from decisions.enums import NODE_TYPE_CHOICES, NODE_TYPE_NON_LEAF


class Condition(models.Model):
    """ Model to hold condition data.

        Here condition is e.g.
        name = age > 75
        value_name = age
        value_type = integer
        operator = >
        value = 75

        Would be equivalent to age > 75
    """
    name = models.CharField(max_length=64, null=False,
                            blank=False, default='', unique=True)
    value_name = models.CharField(max_length=64, null=False,
                                  blank=False, default='')
    value_type = models.PositiveSmallIntegerField(null=False, blank=False,
                                                  choices=VALUE_TYPE_CHOICES,
                                                  default=VALUE_TYPE_BOOLEAN)
    operator = models.PositiveSmallIntegerField(null=False, blank=False,
                                                choices=OPERATOR_CHOICES,
                                                default=OPERATOR_EQUAL_TO)
    value = models.CharField(max_length=64, null=False,
                             blank=False, default='')

    class Meta:
        verbose_name = 'Condition'
        verbose_name_plural = 'Conditions'

    def __str__(self):
        return f'{self.name}'


class Node(models.Model):
    """ Model to hold the decision tree nodes.
    """
    name = models.CharField(max_length=64, null=False,
                            blank=False, default='', unique=True)
    condition = models.ForeignKey('Condition', null=True, blank=True,
                                  on_delete=models.CASCADE)
    node_type = models.PositiveSmallIntegerField(null=False, blank=False,
                                                 choices=NODE_TYPE_CHOICES,
                                                 default=NODE_TYPE_NON_LEAF)

    class Meta:
        verbose_name = 'Node'
        verbose_name_plural = 'Nodes'

    def __str__(self):
        return f'{self.name}'


class DecisionTree(models.Model):
    """ Model to hold the decision tree.
    """

    name = models.CharField(max_length=64, null=False,
                            blank=False, default='', unique=True)

    nodes = models.ManyToManyField('Node', through='DecisionTreeNodeM2M', through_fields=('decision_tree', 'node'))
    
    class Meta:
        verbose_name = 'Decision Tree'
        verbose_name_plural = 'Decision Trees'

    def __str__(self):
        return f'{self.name}'


class DecisionTreeNodeM2M(models.Model):
    """ Model to hold the many to many relationship
        between DecisionTree and Nodes.
    """

    decision_tree = models.ForeignKey('DecisionTree', on_delete=models.CASCADE, related_name='nodes_m2m')
    node = models.ForeignKey('Node', on_delete=models.CASCADE, related_name='+')
    pos_node = models.ForeignKey('Node', on_delete=models.CASCADE, related_name='+')
    neg_node = models.ForeignKey('Node', on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return f'{self.decision_tree} -> {self.node}'

    
class DecisionTreeRuns(models.Model):
    """ Model to hold the results of the decision
        tree runs.
    """
    patient = models.ForeignKey(get_user_model(), null=False, blank=False,
                                on_delete=models.CASCADE)
    decision_tree = models.ForeignKey('DecisionTree', null=False, blank=False,
                                      on_delete=models.CASCADE)
    result = models.CharField(max_length=64, null=False,
                              blank=False, default='')
    datetime = models.DateTimeField(blank=False, null=False, default=timezone.now)

    class Meta:
        verbose_name = 'Decision Tree Run'
        verbose_name_plural = 'Decision Tree Runs'

    def __str__(self):
        return f'{self.patient.uuid} - {self.decision_tree.name} - {self.result}'
