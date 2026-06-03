import 'package:flutter/material.dart';

import '../../../../core/widgets/aegis_card.dart';
import '../../../../core/widgets/aegis_button.dart';
import '../../../../core/widgets/aegis_chip.dart';
import '../../../../core/theme/aegis_spacing.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Executive overview')),
      body: ListView(
        padding: const EdgeInsets.all(AssistanceSpacing.lg),
        children: [
          const AegisCard(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text('Morning briefing'),
                SizedBox(height: AssistanceSpacing.sm),
                Text('You have 3 meetings, 5 tasks, and 2 travel updates.'),
              ],
            ),
          ),
          const SizedBox(height: AssistanceSpacing.lg),
          Row(
            children: const [
              AegisChip(label: 'Focus', variant: AegisChipVariant.subtle),
              SizedBox(width: AssistanceSpacing.sm),
              AegisChip(label: 'Priority', variant: AegisChipVariant.filled),
            ],
          ),
          const SizedBox(height: AssistanceSpacing.lg),
          AegisButton(
            label: 'Plan my day',
            onPressed: () {},
          ),
        ],
      ),
    );
  }
}
