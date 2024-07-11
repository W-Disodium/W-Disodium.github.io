import tkinter as tk
import socket
from threading import Thread
from tkinter import messagebox
from tkinter import filedialog
import os
import json

# 将函数放入线程
def thread_it(func):
    # 创建线程
    t = Thread(target=func)
    # 守护线程
    t.Daemon = True
    # 启动线程
    t.start()


class MainPanel:
    def __init__(self):
        self.main = tk.Tk()
        self.msg_panel = None
        self.btn_color = 'light grey'  # 按钮颜色：淡灰色
        self.socket = None

        self.ip_box = None  # 输入IP的内容
        self.port_box = None  # 输入port的内容
        self.listen_box = None  # 输入监听端口的内容

        self.input_txt = None  # 可修改的文本框，用于输入信息等待发送
        self.msg_txt = None  # 不可编辑的文本框，用于显示聊天记录

        self.send_msg_btn = None  # 发送文本按钮
        self.send_file_btn = None  # 发送文件按钮
        self.listen_btn = None  # 启动监听按钮
        self.send_btn = None  # 发送文本界面的send按钮

        # self.flag_state = 0  # 0：服务端，1：客户端
        # self.flag_conn = 0  # 0：未连接，1：已连接
        # self.flag_file = 0  # 0：发送文本，1：发送文件

        self.ip = None  # 对方IP
        self.host = socket.gethostbyname(socket.gethostname())  # 本机ip

    # 创建空的主界面，设置基本内容
    def set_main(self):
        width = 450
        height = 300
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        gm_str = '%dx%d+%d+%d' % (width, height, (screen_width - width) / 2,
                                  (screen_height - 1.2 * height) / 2)
        self.main.geometry(gm_str)
        title = socket.gethostbyname(socket.gethostname())
        self.main.title(title)

    # 接收方信息
    def set_receiver(self):
        # 框架
        receiver_frame = tk.Frame(self.main, pady=5)
        receiver_frame.pack()

        # 文本显示
        tk.Label(receiver_frame, text='接收方IP：').grid(row=0, column=0)
        # IP 和 port输入框
        self.ip_box = tk.StringVar()
        tk.Entry(receiver_frame,
                 textvariable=self.ip_box,
                 width=30).grid(row=0, column=1)
        self.port_box = tk.StringVar()
        tk.Entry(receiver_frame,
                 textvariable=self.port_box,
                 width=10).grid(row=0, column=3)
        # 文本显示
        tk.Label(receiver_frame, text='端口：').grid(row=0, column=2, ipadx=5)

    # 发送按钮的一行，发送文本按钮和文件按钮分别有choice_txt和choice_file两个函数，开线程
    def set_send(self):
        # 框架
        send_frame = tk.Frame(self.main, pady=5)
        send_frame.pack()

        # 发送文本按钮
        self.send_msg_btn = tk.Button(send_frame,
                                      text='发送文本',
                                      bg=self.btn_color,
                                      width=17,
                                      command=lambda: thread_it(self.choice_txt))
        self.send_msg_btn.grid(row=0, column=0, padx=17)
        # 发送文件按钮
        self.send_file_btn = tk.Button(send_frame, text='发送文件',
                                       bg=self.btn_color,
                                       width=17,
                                       command=lambda: thread_it(self.choice_file))
        self.send_file_btn.grid(row=0, column=1, padx=17)

    # 监听端口和按钮的一行，监听按钮有listening函数，开线程
    def set_listen(self):
        # 框架
        listen_frame = tk.Frame(self.main, pady=5)
        listen_frame.pack()

        # 文本显示
        tk.Label(listen_frame, text='本机监听接口：').grid(row=0, column=0)
        # 监听输入框
        self.listen_box = tk.StringVar()
        tk.Entry(listen_frame,
                 textvariable=self.listen_box,
                 width=10).grid(row=0, column=1)
        # 启动监听按钮
        self.listen_btn = tk.Button(listen_frame,
                                    text='启动监听',
                                    bg=self.btn_color,
                                    width=17,
                                    command=lambda: thread_it(self.listening))
        self.listen_btn.grid(row=0, column=2, padx=30)

    # 消息框和清空按钮，清空按钮有clr_msg函数，开线程
    def set_msg(self):
        # 框架
        msg_frame = tk.Frame(self.main, pady=5)
        msg_frame.pack()

        # 文本框
        self.msg_txt = tk.Text(msg_frame, width=55, height=9)
        self.msg_txt.config(state=tk.DISABLED)  # 设置消息框为不可修改状态
        self.msg_txt.grid(row=0, pady=5)
        # 清除按钮
        clr_btn = tk.Button(msg_frame,
                            text='清空消息框',
                            bg=self.btn_color,
                            width=17,
                            command=lambda: thread_it(self.clr_msg))
        clr_btn.grid(row=1)

    # 展示界面
    def show(self):
        self.set_main()
        self.set_receiver()
        self.set_send()
        self.set_listen()
        self.set_msg()
        self.main.mainloop()

    def clr_msg(self):
        self.msg_txt.config(state=tk.NORMAL)
        self.msg_txt.delete(0.0, self.msg_txt.get(0.0, tk.END).__len__() - 1.0)
        self.msg_txt.config(state=tk.DISABLED)

    # 服务端建立连接
    def server_conn(self):
        if self.socket is None:  # 未连接的服务端
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind((self.host, int(self.listen_box.get().strip())))
            server.listen(5)
            while True:
                try:
                    self.socket, addr = server.accept()
                    self.ip = addr[0]
                    thread_it(self.receiving)  # 持续接收信息
                    return 1
                except:
                    self.socket = None
                    return 0
        return 1

    # 客户端建立连接
    def client_conn(self):
        if self.socket is None:  # 未连接的服务端
            try:
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.connect((self.ip_box.get(), int(self.port_box.get().strip())))
                self.ip = self.ip_box.get()
                thread_it(self.receiving)  # 开始持续接收消息
                return 1
            except:
                self.socket = None
                messagebox.showwarning('Warning', message='未建立连接，请检查信息填写。')
                return 0
        return 1

    # 持续接收信息
    def receiving(self):
        while True:
            recv_flag = self.socket.recv(1024).decode('utf-8')
            if recv_flag == '1':
                recv_data = self.socket.recv(1024)
                self.msg_txt.config(state=tk.NORMAL)
                self.msg_txt.insert(tk.END, 'From：' + self.ip + '：' + recv_data.decode('utf-8'))
                self.msg_txt.config(state=tk.DISABLED)
            else:
                max_len = 8388608
                msg_header = self.socket.recv(1024)
                header = eval(msg_header.decode('utf-8'))  # 包含信息的字典
                msg = '收到文件' + str(header['filename']) + header['msg_type'] + '，是否接收？'
                flag = tk.messagebox.askyesno(title='Recv File', message=msg)
                if flag:
                    recv_path = filedialog.askdirectory(title='选择接受文件夹')
                    filename = recv_path + '\\recv_' + str(header['filename']) + header['msg_type']
                    get_file_size = header['msg_len']
                    file_size = 0
                    with open(filename, 'wb') as fp:
                        while file_size != get_file_size:
                            message = self.socket.recv(max_len)
                            fp.write(message)
                            file_size += len(message)
                    self.msg_txt.config(state=tk.NORMAL)
                    self.msg_txt.insert(tk.END, '已接收' + str(header['filename']) + header['msg_type'] + '\n')
                    self.msg_txt.config(state=tk.DISABLED)
                else:
                    get_file_size = header['msg_len']
                    file_size = 0
                    while file_size != get_file_size:
                        message = self.socket.recv(max_len)
                        file_size += len(message)

    # 选择文本，确认是否建立连接，跳出新窗口，发送
    def choice_txt(self):
        if self.client_conn() == 1:
            self.msg_panel = tk.Toplevel(self.main)
            self.msg_panel.geometry('+580+210')
            self.msg_panel.grab_set()

            self.input_txt = tk.Text(self.msg_panel, width=50, height=15)
            self.input_txt.pack()

            self.send_msg_btn = tk.Button(self.msg_panel,
                                          text='Send',
                                          bg=self.btn_color,
                                          width=17,
                                          command=lambda: thread_it(self.sending))
            self.send_msg_btn.pack(pady=5)

    # 点击send按钮后发送文本
    def sending(self):
        txt = self.input_txt.get(0.0, tk.END)
        self.socket.send('1'.encode('utf-8'))
        self.socket.send(txt.encode('utf-8'))

        self.msg_txt.config(state=tk.NORMAL)
        self.msg_txt.insert(tk.END, 'By Me：' + txt)
        self.msg_txt.config(state=tk.DISABLED)

        self.msg_panel.destroy()

    # 发送文件：确认建立连接，选择发送的文件，发送标识符和文件
    def choice_file(self):
        if self.client_conn() == 1:
            max_len = 8388608
            filepath = filedialog.askopenfilename(title='选择传输文件')  # filepath = 路径+文件名
            if filepath != '':
                filename = filepath.split('/')[-1]  # filename = 文件名
                file, class_file = os.path.splitext(filename)
                file_size = os.stat(filepath).st_size
                msg_header = {'filename': file, 'msg_type': class_file, 'msg_len': file_size}
                msg_header_bytes = bytes(json.dumps(msg_header), encoding='utf-8')
                # 当消息头的长度不满1024时，使用空格填充
                msg_header_bytes += b'' * (max_len - len(msg_header_bytes))
                # 发送文档标识，发送消息头
                self.socket.send('0'.encode('utf-8'))
                self.socket.send(msg_header_bytes)
                file_len = 0
                recv_count = 0
                with open(filepath, 'rb') as fp:
                    while file_len != file_size:
                        message = fp.read(max_len)
                        self.socket.send(message)
                        file_len += len(message)
                        recv_count += 1
                self.msg_txt.config(state=tk.NORMAL)
                self.msg_txt.insert(tk.END, '已发送' + filename + '\n')
                self.msg_txt.config(state=tk.DISABLED)

    # 监听
    def listening(self):
        port = self.listen_box.get().strip()
        if port == '':
            messagebox.showwarning('Warning', message='请填写完整信息！')
        else:
            self.listen_btn['text'] = '监听中……'
            self.listen_btn['bg'] = 'pale green'
            self.server_conn()


if __name__ == '__main__':
    test = MainPanel()
    test.show()
