# operating-contour-next-link
Electronic interface to HMI of Contour Next Link

The Contour Next Link 2.4 is operated using micro-relays soldered in parallel with the push button switches, closing for push.

![screen shot 2016-12-30 at 22 35 03](https://cloud.githubusercontent.com/assets/16906631/21573767/5d6145a0-cee0-11e6-8154-ed23beefb9c2.png)

Top level demo is Test_CNL24.py. Specific pin allocation is set in the CNLIO class in CNLIO-Pi.py, code is to suit configuration shown in circuit diagram below.

![circuit_pi](https://cloud.githubusercontent.com/assets/16906631/21573850/7e78f8d6-cee1-11e6-8e2d-c609f038866b.png)

Typical solid state micro-relay: https://github.com/Bal00/operating-contour-next-link/files/679303/0900766b8131432d.pdf
