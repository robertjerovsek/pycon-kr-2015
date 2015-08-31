# -*- coding: utf-8 -*-

from locust import HttpLocust, TaskSet, task


class LoadTestTasks(TaskSet):
    @task
    def customer_path(self):

        # Look at 4 different products

        for i in range(4):
            self.client.get(url='/', name='1. index')
            self.client.get(url='/product', name='2. product')

        # Finally buy a product

        self.client.post(url='/buy', name='3. buy')


class LoadTestLocust(HttpLocust):
    task_set = LoadTestTasks
    min_wait = 0
    max_wait = 0
