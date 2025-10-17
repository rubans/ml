# define custom agent - convert pdf to pngs
class ConverPDFAgent(BaseChatAgent):
    def __init__(self, name: str, input_path: str, output_path: str, zoom: float=2.0):
        super().__init__(name, "An agent that convers PDFs to Images.")
        self._input_path = input_path
        self._output_path = output_path
        self._zoom = zoom

    @property
    def produced_message_types(self) -> Sequence[type[ChatMessage]]:
        return (TextMessage,)

    async def on_messages(self, messages: Sequence[ChatMessage], cancellation_token: CancellationToken) -> Response:
        # Calls the on_messages_stream.
        response: Response | None = None
        async for message in self.on_messages_stream(messages, cancellation_token):
            if isinstance(message, Response):
                response = message
        assert response is not None
        return response

    async def on_messages_stream(
        self, messages: Sequence[ChatMessage], cancellation_token: CancellationToken
    ) -> AsyncGenerator[AgentEvent | ChatMessage | Response, None]:
        inner_messages: List[AgentEvent | ChatMessage] = []
        with fitz.open(self._input_path) as pdf_document:
            if not os.path.exists(self._output_path):
                os.makedirs(self._output_path)
            # Loop through each page in the PDF
            for page_num in range(len(pdf_document)):
                page = pdf_document[page_num]
                # Zoom factor: higher zoom increases resolution
                mat = fitz.Matrix(self._zoom, self._zoom)
                pix = page.get_pixmap(matrix=mat)  # Render page to an image
                # Save the image
                output_file = os.path.join(self._output_path, f"page_{page_num + 1}.png")
                pix.save(output_file)
                msg = TextMessage(content=f"processing page_{page_num + 1}..", source=self.name)
                inner_messages.append(msg)
                yield msg
        yield Response(chat_message=TextMessage(content="Done!", source=self.name), inner_messages=inner_messages)

    async def on_reset(self, cancellation_token: CancellationToken) -> None:
        pass


# # debug run
# async def run_agent() -> None:
#     # Create an agent.
#     pdf_converter_agent = ConverPDFAgent("pdf_converter",pdf_path,output_dir)
#     # Run the agent with a given task and stream the response.
#     async for message in pdf_converter_agent.on_messages_stream([], CancellationToken()):
#         if isinstance(message, Response):
#             print(message.chat_message.content)
#         else:
#             print(message.content)


# # Use asyncio.run(run_countdown_agent()) when running in a script.
# await run_agent()