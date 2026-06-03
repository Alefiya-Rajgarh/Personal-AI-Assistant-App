import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import '../../../../core/widgets/aegis_button.dart';
import '../../../../core/widgets/aegis_card.dart';
import '../../../../core/theme/aegis_spacing.dart';

class OnboardingScreen extends StatelessWidget {
  const OnboardingScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(AssistanceSpacing.lg),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                'Your AI executive team',
                style: Theme.of(context).textTheme.displayMedium,
              ),
              const SizedBox(height: AssistanceSpacing.sm),
              Text(
                'Coordinate tasks, travel, and meetings with a single command center.',
                style: Theme.of(context).textTheme.bodyLarge,
              ),
              const SizedBox(height: AssistanceSpacing.lg),
              const AegisCard(
                child: Text('Connect your calendar, inbox, and memory vaults.'),
              ),
              const Spacer(),
              AegisButton(
                label: 'Get Started',
                onPressed: () => context.go('/auth/login'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
