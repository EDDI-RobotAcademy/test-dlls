from user_defined_queue.service.user_defined_queue_service_impl import UserDefinedQueueServiceImpl


class UserDefinedInitializer:
    @staticmethod
    def initUserDefinedQueueDomain():
        userDefinedQueueService = UserDefinedQueueServiceImpl.getInstance()
        userDefinedQueueService.createUserDefinedQueue()

    @staticmethod
    def initUserDefinedDomain():
        UserDefinedInitializer.initUserDefinedQueueDomain()