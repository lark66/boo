import HTMLTestRunner

if __name__ == '__main__':
    filePath = '/Users/aina/PycharmProjects/ROS/report/run_main.py'
    fp = file(filePath)
    runner =HTMLTestRunner.HTMLTestRunner(
        stream =fp,
        title =u'b报告',
        tester=u'aina')
    runner.run(Suite())