from manim import *

class VolumetricVideoReportFixed(Scene):
    def construct(self):
        my_font = "sans-serif"
        
        # ==========================================
        # SCENE 1: TITLE & INTRODUCTION
        # ==========================================
        title_1 = Text("BÁO CÁO VOLUMETRIC VIDEO", font=my_font, weight=BOLD, color=BLUE).scale(1.2)
        title_2 = Text("IN THE REAL WORLD", font=my_font, weight=BOLD, color=TEAL).scale(1.1)
        title_3 = Text("(CVPR 2025)", font=my_font, font_size=24, color=GRAY)
        
        VGroup(title_1, title_2, title_3).arrange(DOWN, buff=0.5)
        
        self.play(Write(title_1), run_time=2.5)
        self.play(FadeIn(title_2, shift=UP), run_time=2)
        self.play(FadeIn(title_3), run_time=1.5)
        self.wait(5)
        
        self.play(FadeOut(VGroup(title_1, title_2, title_3)), run_time=2)

        # ==========================================
        # SCENE 2: OVERVIEW
        # ==========================================
        header_overview = Text("I. Tổng quan về Video Không gian", font=my_font, color=YELLOW).to_edge(UP)
        self.play(Write(header_overview), run_time=2)

        def_text = Text(
            "Video không gian mã hóa cảnh 3D thay đổi theo thời gian\n"
            "thành biểu diễn thống nhất (novel-view synthesis).",
            font=my_font, font_size=28, color=GRAY
        )
        self.play(FadeIn(def_text, shift=RIGHT), run_time=2)
        self.wait(8)
        self.play(def_text.animate.shift(UP*2).scale(0.8), run_time=2)

        chal_title = Text("Thách thức chính:", font=my_font, font_size=32, color=RED).next_to(def_text, DOWN, buff=1).align_to(def_text, LEFT)
        self.play(Write(chal_title), run_time=1.5)

        bullets_overview = VGroup(
            Text("• Chi phí tính toán & lưu trữ lớn cho hình ảnh động.", font=my_font, font_size=24),
            Text("• Khó khăn đặc thù: con người, trong nhà, và đô thị lớn.", font=my_font, font_size=24),
            Text("• Khắc phục chi phí phần cứng đa camera đắt đỏ.", font=my_font, font_size=24),
            Text("• Tương lai: Dữ liệu 4D làm 'biểu diễn trung gian'.", font=my_font, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(chal_title, DOWN, buff=0.5).align_to(chal_title, LEFT)

        for bullet in bullets_overview:
            self.play(FadeIn(bullet, shift=UP), run_time=2)
            self.wait(6) 

        self.play(FadeOut(VGroup(def_text, chal_title, bullets_overview)), run_time=2)

        # ==========================================
        # SCENE 3: MONOCULAR INPUTS (ĐÃ FIX LỖI CHÌM CHỮ)
        # ==========================================
        header_mono = Text("1. Generating Volumetric Video from Monocular Inputs", font=my_font, font_size=32, color=YELLOW).to_edge(UP)
        self.play(Transform(header_overview, header_mono), run_time=2)

        speaker_1 = Text("Diễn giả: Aleksander Holynski (Google DeepMind)", font=my_font, font_size=24, color=BLUE)
        mono_prob = Text("Vấn đề: Thiếu chiều sâu và bị che khuất khi dùng 1 camera.", font=my_font, font_size=26)

        box = Square(side_length=1.8, color=WHITE)
        question_mark = Text("?", font_size=40).move_to(box.get_center())
        box_group = VGroup(box, question_mark)
        
        sol_1 = Text("Giải pháp: Diffusion Models ảo giác (hallucinate) các phần bị che khuất.", font=my_font, font_size=24)
        impact_1 = Text("Ý nghĩa: Tạo video 3D chỉ bằng smartphone thông thường.", font=my_font, font_size=26, color=ORANGE)

        # Gom nhóm toàn bộ Scene 3 và ép kích thước để không bao giờ bị tràn
        scene_3 = VGroup(speaker_1, mono_prob, box_group, sol_1, impact_1).arrange(DOWN, buff=0.5)
        scene_3.next_to(header_mono, DOWN, buff=0.4)
        if scene_3.height > 5.5:
            scene_3.scale_to_fit_height(5.5)
            scene_3.next_to(header_mono, DOWN, buff=0.4)

        self.play(FadeIn(speaker_1), run_time=1.5)
        self.play(Write(mono_prob), run_time=2)
        self.wait(5)
        self.play(Create(box), Write(question_mark), run_time=2)
        self.play(Write(sol_1), run_time=2.5)
        self.wait(6)

        # Thiết lập vị trí Brain theo box đã được bóp kích thước (nếu có)
        brain = Circle(color=GREEN).match_width(box).move_to(box.get_center())
        check = Text("3D", font=my_font, font_size=40, color=GREEN).match_height(question_mark).move_to(brain.get_center())
        
        self.play(Transform(box, brain), Transform(question_mark, check), run_time=2)
        self.wait(5)
        self.play(FadeIn(impact_1, shift=UP), run_time=2)
        self.wait(10)
        self.play(FadeOut(scene_3), run_time=2)

        # ==========================================
        # SCENE 4: DYNAMIC 4D HUMANS (ĐÃ FIX LỖI CHÌM CHỮ)
        # ==========================================
        header_humans = Text("2. Dynamic 4D Humans", font=my_font, font_size=32, color=YELLOW).to_edge(UP)
        self.play(Transform(header_overview, header_humans), run_time=2)

        speaker_2 = Text("Diễn giả: Lan Xu (ShanghaiTech)", font=my_font, font_size=24, color=BLUE)
        human_prob = Text("Vấn đề: Tái tạo chi tiết khớp nối, da, tóc và quần áo rất khó.", font=my_font, font_size=26)

        circle_motion = Circle(radius=1, color=RED)
        text_motion = Text("Motion\n(Khung xương)", font=my_font, font_size=20).move_to(circle_motion.get_center())
        group_motion = VGroup(circle_motion, text_motion)
        
        circle_appearance = Circle(radius=1, color=BLUE)
        text_app = Text("Appearance\n(Bề mặt)", font=my_font, font_size=20).move_to(circle_appearance.get_center())
        group_app = VGroup(circle_appearance, text_app)

        graphics_4 = VGroup(group_motion, group_app).arrange(RIGHT, buff=1.5)

        sol_2 = Text("Giải pháp: Tách biệt Motion và Appearance bằng Dual-Gaussian.", font=my_font, font_size=24)
        impact_2 = Text("Ứng dụng: Hệ thống 'Reperformer' - Điều khiển người biểu diễn 3D.", font=my_font, font_size=26, color=ORANGE)

        # Gom nhóm toàn bộ Scene 4 và ép kích thước để không bao giờ bị tràn
        scene_4 = VGroup(speaker_2, human_prob, graphics_4, sol_2, impact_2).arrange(DOWN, buff=0.5)
        scene_4.next_to(header_humans, DOWN, buff=0.4)
        if scene_4.height > 5.5:
            scene_4.scale_to_fit_height(5.5)
            scene_4.next_to(header_humans, DOWN, buff=0.4)

        self.play(FadeIn(speaker_2), run_time=1.5)
        self.play(Write(human_prob), run_time=2)
        self.wait(8)
        self.play(Create(group_motion), Create(group_app), run_time=3)
        self.wait(5)
        self.play(FadeIn(sol_2, shift=UP), run_time=2)
        self.wait(8)
        self.play(Write(impact_2), run_time=2.5)
        self.wait(12)
        self.play(FadeOut(scene_4), run_time=2)

        # ==========================================
        # SCENE 5: IMMERSIVE SPACES
        # ==========================================
        header_spaces = Text("3. Immersive & Dynamic Spaces", font=my_font, font_size=32, color=YELLOW).to_edge(UP)
        self.play(Transform(header_overview, header_spaces), run_time=2)

        speaker_3 = Text("Diễn giả: Christian Richardt (Meta Reality Labs)", font=my_font, font_size=24, color=BLUE)
        space_prob = Text("Vấn đề: Render vật lý ánh sáng/âm thanh trên kính VR tốn tài nguyên.", font=my_font, font_size=24)

        bullets_spaces = VGroup(
            Text("• NeRF + SDF giảm số lượng mẫu (samples) tính toán.", font=my_font, font_size=22),
            Text("• Real Acoustics Fields: Tổng hợp âm thanh không gian dội âm.", font=my_font, font_size=22),
            Text("• Cảm biến Time-of-Flight khắc phục vùng tối, phản chiếu.", font=my_font, font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        scene_5 = VGroup(speaker_3, space_prob, bullets_spaces).arrange(DOWN, buff=0.8)
        scene_5.next_to(header_spaces, DOWN, buff=0.5)
        if scene_5.height > 5.5:
            scene_5.scale_to_fit_height(5.5)
            scene_5.next_to(header_spaces, DOWN, buff=0.5)

        self.play(FadeIn(speaker_3), run_time=1.5)
        self.play(Write(space_prob), run_time=2.5)
        self.wait(8)
        for b in bullets_spaces:
            self.play(FadeIn(b, shift=RIGHT), run_time=2.5)
            self.wait(8)

        self.play(FadeOut(scene_5), run_time=2)

        # ==========================================
        # SCENE 6: AUTONOMOUS VEHICLES (ĐÃ KHÔI PHỤC TOÀN BỘ CHỮ GỐC)
        # ==========================================
        header_av = Text("4. Volumetric Video in Autonomous Vehicles", font=my_font, font_size=32, color=YELLOW).to_edge(UP)
        self.play(Transform(header_overview, header_av), run_time=2)

        speaker_4 = Text("Diễn giả: Boris Ivanovic (NVIDIA)", font=my_font, font_size=24, color=BLUE)
        av_prob = Text("Vấn đề: Thử nghiệm thực tế đắt đỏ, mô phỏng cũ thiếu sai số tích lũy.", font=my_font, font_size=24)

        car = Rectangle(width=2, height=1, color=TEAL)
        car_text = Text("AV AI", font=my_font, font_size=20).move_to(car.get_center())
        loop_arrow = CurvedArrow(start_point=RIGHT*2, end_point=LEFT*2, angle=TAU/2, color=YELLOW)
        loop_arrow.next_to(car, DOWN, buff=0.5)
        loop_text = Text("Closed-loop Simulation", font=my_font, font_size=20).next_to(loop_arrow, DOWN, buff=0.2)
        av_sim_graphics = VGroup(car, car_text, loop_arrow, loop_text)

        av_sol = Text("Giải pháp: NeRF/Gaussian Splats + DreamDrive (Video Gen Models) tạo góc nhìn.", font=my_font, font_size=20)

        scene_6 = VGroup(speaker_4, av_prob, av_sim_graphics, av_sol).arrange(DOWN, buff=0.5)
        scene_6.next_to(header_av, DOWN, buff=0.4)
        if scene_6.height > 5.5:
            scene_6.scale_to_fit_height(5.5)
            scene_6.next_to(header_av, DOWN, buff=0.4)

        self.play(FadeIn(speaker_4), run_time=1.5)
        self.play(Write(av_prob), run_time=2.5)
        self.wait(8)
        self.play(Create(av_sim_graphics), run_time=4)
        self.wait(6)
        self.play(FadeIn(av_sol, shift=UP), run_time=2)
        self.wait(10)
        self.play(FadeOut(scene_6), run_time=2)

        # ==========================================
        # SCENE 7: COMPRESSION
        # ==========================================
        header_comp = Text("5. Compression and Standardization of Gaussian Splats", font=my_font, font_size=28, color=YELLOW).to_edge(UP)
        self.play(Transform(header_overview, header_comp), run_time=2)

        speaker_5 = Text("Diễn giả: Yiyi Liao (Zhejiang University)", font=my_font, font_size=24, color=BLUE)
        comp_prob = Text("Vấn đề: Gaussian Splats tốn hàng GB lưu trữ, cản trở truyền tải mạng.", font=my_font, font_size=22)

        bullets_comp = VGroup(
            Text("• Huấn luyện tích hợp mô phỏng nén ngay từ đầu.", font=my_font, font_size=22),
            Text("• Lượng tử hóa & Giảm Entropy để giảm dung lượng.", font=my_font, font_size=22),
            Text("• Không gian gốc + Thuộc tính thay đổi thời gian (Bitrate < 50 Mbps).", font=my_font, font_size=22),
            Text("• Tiêu chuẩn hóa MPEG cho mã hóa công nghiệp.", font=my_font, font_size=22, color=ORANGE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        scene_7 = VGroup(speaker_5, comp_prob, bullets_comp).arrange(DOWN, buff=0.8)
        scene_7.next_to(header_comp, DOWN, buff=0.5)
        if scene_7.height > 5.5:
            scene_7.scale_to_fit_height(5.5)
            scene_7.next_to(header_comp, DOWN, buff=0.5)

        self.play(FadeIn(speaker_5), run_time=1.5)
        self.play(Write(comp_prob), run_time=2.5)
        self.wait(8)
        for b in bullets_comp:
            self.play(FadeIn(b, shift=LEFT), run_time=2.5)
            self.wait(8)
        self.play(FadeOut(scene_7), run_time=2)

        # ==========================================
        # SCENE 8: REAL-TIME STREAMING (ĐÃ KHÔI PHỤC TOÀN BỘ CHỮ GỐC)
        # ==========================================
        header_stream = Text("6. Efficient real-time streaming of volumetric video", font=my_font, font_size=28, color=YELLOW).to_edge(UP)
        self.play(Transform(header_overview, header_stream), run_time=2)

        speaker_6 = Text("Diễn giả: Sharath Girish (Snap Inc.)", font=my_font, font_size=24, color=BLUE)
        stream_prob = Text("Vấn đề: Gọi video 3D đòi hỏi cập nhật và giải mã liên tục (online).", font=my_font, font_size=22)

        grid = NumberPlane(x_range=[-2, 2], y_range=[-1, 1], background_line_style={"stroke_opacity": 0.2}).scale(0.8)
        
        stream_sol = Text("Giải pháp: Cập nhật phần dư (Attribute Residuals).", font=my_font, font_size=22)
        stream_sol2 = Text("Phân bổ thưa thớt (chỉ cập nhật điểm bị động).", font=my_font, font_size=22)
        impact_6 = Text("Ý nghĩa: Giảm 10x dung lượng, giữ render thời gian thực.", font=my_font, font_size=22, color=GREEN)

        scene_8 = VGroup(speaker_6, stream_prob, grid, stream_sol, stream_sol2, impact_6).arrange(DOWN, buff=0.4)
        scene_8.next_to(header_stream, DOWN, buff=0.4)
        if scene_8.height > 5.5:
            scene_8.scale_to_fit_height(5.5)
            scene_8.next_to(header_stream, DOWN, buff=0.4)

        # Khởi tạo chấm đỏ sau khi grid đã được bóp kích thước
        dot = Dot(color=RED).move_to(grid.c2p(0, 0))

        self.play(FadeIn(speaker_6), run_time=1.5)
        self.play(Write(stream_prob), run_time=2.5)
        self.wait(8)
        self.play(Create(grid), FadeIn(dot), run_time=2)
        
        self.play(Write(stream_sol), run_time=2)
        self.wait(5)
        self.play(dot.animate.move_to(grid.c2p(1, 0.5)), run_time=2)
        self.play(Write(stream_sol2), run_time=2)
        self.wait(8)
        self.play(FadeIn(impact_6, scale=1.2), run_time=2.5)
        self.wait(12)

        self.play(FadeOut(scene_8), FadeOut(dot), run_time=2)

        # ==========================================
        # SCENE 9: CONCLUSION & REFERENCES
        # ==========================================
        self.play(FadeOut(header_overview), run_time=1)
        
        thank_you = Text("CẢM ƠN ĐÃ THEO DÕI", font=my_font, font_size=40, weight=BOLD, color=BLUE).shift(UP*1)
        ref_title = Text("References:", font=my_font, font_size=24, color=YELLOW).next_to(thank_you, DOWN, buff=1)
        ref_text = Text(
            "Videos, C. (2025, June 11). Volumetric Video in the Real World [Video].\n"
            "Retrieved from YouTube: https://www.youtube.com/watch?v=AumlqB08V7c",
            font=my_font, font_size=18, color=GRAY
        ).next_to(ref_title, DOWN, buff=0.5)

        self.play(Write(thank_you), run_time=3)
        self.play(FadeIn(ref_title), FadeIn(ref_text), run_time=3)
        self.wait(15) 
        self.play(FadeOut(Group(*self.mobjects)), run_time=3)