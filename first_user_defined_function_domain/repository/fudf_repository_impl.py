import json
import queue

from first_user_defined_function_domain.repository.fudf_repository import FirstUserDefinedFunctionDomainRepository


class FirstUserDefinedFunctionDomainRepositoryImpl(FirstUserDefinedFunctionDomainRepository):
    def getResult(self, userDefinedReceiverFastAPIChannel):
        print(f"FirstUserDefinedFunctionDomainRepositoryImpl getResult()")

        try:
            receivedResponseFromSocketClient = userDefinedReceiverFastAPIChannel.get(False)
            return json.loads(receivedResponseFromSocketClient)

        except queue.Empty:
            return "아직 데이터를 처리 중이거나 요청한 데이터가 없습니다"
